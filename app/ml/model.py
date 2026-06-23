
import torch
import torch.nn as nn

class ForecastModel(nn.Module):
    def __init__(self, input_size=5):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_size, 32),
            nn.ReLU(),
            nn.Linear(32, 1)
        )

    def forward(self, x):
        return self.net(x)
