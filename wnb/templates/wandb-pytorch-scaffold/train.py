# last_verified: 2026-07-30 · wnb n/a

"""PyTorch training script with W&B experiment tracking.

Logs hyperparameters, metrics, and model artifacts to W&B.
Designed for use in CI/CD pipelines and local development.
"""

import argparse
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

import wandb


def build_model(input_dim, hidden_dim, output_dim):
    model = nn.Sequential(
        nn.Linear(input_dim, hidden_dim),
        nn.ReLU(),
        nn.Linear(hidden_dim, output_dim),
    )
    return model


def train_epoch(model, loader, criterion, optimizer, device):
    model.train()
    total_loss = 0.0
    for inputs, targets in loader:
        inputs, targets = inputs.to(device), targets.to(device)
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()
        total_loss += loss.item() * inputs.size(0)
    return total_loss / len(loader.dataset)


def evaluate(model, loader, criterion, device):
    model.eval()
    total_loss = 0.0
    correct = 0
    total = 0
    with torch.no_grad():
        for inputs, targets in loader:
            inputs, targets = inputs.to(device), targets.to(device)
            outputs = model(inputs)
            loss = criterion(outputs, targets)
            total_loss += loss.item() * inputs.size(0)
            preds = outputs.argmax(dim=1)
            correct += (preds == targets).sum().item()
            total += targets.size(0)
    accuracy = correct / total if total > 0 else 0.0
    return total_loss / len(loader.dataset), accuracy


def main():
    parser = argparse.ArgumentParser(description="Train a PyTorch model with W&B tracking")
    parser.add_argument("--epochs", type=int, default=10)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--lr", type=float, default=0.001)
    parser.add_argument("--hidden-dim", type=int, default=64)
    parser.add_argument("--project", default="wandb-pytorch-scaffold")
    parser.add_argument("--entity", default=None)
    args = parser.parse_args()

    run = wandb.init(project=args.project, entity=args.entity, job_type="train")
    wandb.config.update(vars(args))

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    X = torch.randn(1000, 20)
    y = torch.randint(0, 3, (1000,))
    dataset = TensorDataset(X, y)
    loader = DataLoader(dataset, batch_size=args.batch_size, shuffle=True)

    model = build_model(input_dim=20, hidden_dim=args.hidden_dim, output_dim=3).to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=args.lr)

    for epoch in range(args.epochs):
        train_loss = train_epoch(model, loader, criterion, optimizer, device)
        val_loss, val_acc = evaluate(model, loader, criterion, device)
        wandb.log({"epoch": epoch, "train_loss": train_loss, "val_loss": val_loss, "val_accuracy": val_acc})

    torch.save(model.state_dict(), "model.pt")
    wandb.save("model.pt")
    run.finish()


if __name__ == "__main__":
    main()