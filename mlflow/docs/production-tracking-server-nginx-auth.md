# Production MLflow Tracking Server with Nginx Auth Proxy

## Purpose

Deploy an MLflow Tracking Server behind an Nginx reverse proxy with HTTP basic authentication. This lets a team share a single tracking server on a VM or internal network without exposing the backend store port or relying on cloud-managed auth.

## Prerequisites

- Linux VM (tested on Ubuntu 22.04)
- Python 3.8+ and pip
- `nginx` installed (`sudo apt install nginx`)
- `htpasswd` available (`sudo apt install apache2-utils`)
- Network access to port 443 (or a custom port) on the VM

## Steps

### 1. Set up the MLflow Tracking Server

Install MLflow and create a directory for the artifact store:

```bash
pip install mlflow
mkdir -p /var/mlflow/artifacts /var/mlflow/db
```

Start MLflow with a SQLite backend store and a local artifact store:

```bash
mlflow server \
  --backend-store-uri sqlite:///var/mlflow/db/mlflow.db \
  --default-artifact-root /var/mlflow/artifacts \
  --host 127.0.0.1 \
  --port 5000
```

Binding to `127.0.0.1` ensures only the local Nginx proxy can reach it, not external clients.

### 2. Create Nginx credentials

```bash
sudo htpasswd -c /etc/nginx/.htpasswd mlflowuser
```

This prompts for a password and stores a bcrypt hash. Add more users later without `-c` to avoid overwriting the file.

### 3. Configure Nginx reverse proxy

Create `/etc/nginx/sites-available/mlflow-tracking`:

```nginx
server {
    listen 443 ssl;
    server_name mlflow.example.com;

    ssl_certificate     /etc/ssl/certs/example.crt;
    ssl_certificate_key /etc/ssl/private/example.key;

    auth_basic "MLflow Tracking Server";
    auth_basic_user_file /etc/nginx/.htpasswd;

    location / {
        proxy_pass http://127.0.0.1:5000;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Enable the site and reload Nginx:

```bash
sudo ln -s /etc/nginx/sites-available/mlflow-tracking /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### 4. Start MLflow as a systemd service

Create `/etc/systemd/system/mlflow-tracking.service`:

```ini
[Unit]
Description=MLflow Tracking Server
After=network.target

[Service]
User=mlflow
Group=mlflow
WorkingDirectory=/var/mlflow
ExecStart=/usr/local/bin/mlflow server \
  --backend-store-uri sqlite:///var/mlflow/db/mlflow.db \
  --default-artifact-root /var/mlflow/artifacts \
  --host 127.0.0.1 \
  --port 5000
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable mlflow-tracking
sudo systemctl start mlflow-tracking
```

### 5. Connect clients with auth

Clients set the tracking URI and pass credentials in the environment:

```bash
export MLFLOW_TRACKING_URI="https://mlflow.example.com"
export MLFLOW_TRACKING_USERNAME="mlflowuser"
export MLFLOW_TRACKING_PASSWORD="thepassword"
```

Or inline in Python:

```python
import mlflow

mlflow.set_tracking_uri("https://mlflow.example.com")
# Credentials are read from MLFLOW_TRACKING_USERNAME/PASSWORD by default
```

If the server uses a self-signed certificate, set `MLFLOW_TRACKING_INSECURE_TLS=true` or point `MLFLOW_TRACKING_CLIENT_CERT_PATH` at a custom CA.

## Verify

1. Visit `https://mlflow.example.com` in a browser — Nginx should prompt for credentials, then show the MLflow UI.
2. Run a quick training script with `mlflow.set_tracking_uri(...)` pointing at the proxied URL — the run should appear in the UI.
3. Check the Nginx access log at `/var/log/nginx/access.log` for 200 or 401 status codes.

## Common errors

- **MLflow binds to 0.0.0.0 instead of 127.0.0.1** — clients can bypass Nginx and hit MLflow directly. Double-check the `--host` flag.
- **Nginx returns 502 Bad Gateway** — MLflow is not running or is bound to a different port. Run `sudo systemctl status mlflow-tracking` and check `journalctl -u mlflow-tracking`.
- **`htpasswd` not found** — the `apache2-utils` package may not be installed on minimal images. Install it explicitly.
- **Self-signed cert errors on the client** — use `MLFLOW_TRACKING_INSECURE_TLS=true` for testing, or add the CA to the client's trust store for production.
