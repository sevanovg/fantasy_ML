import torch.nn as nn
import torch

class NonLinear(nn.Module):
  def __init__(self, input_dim: int, hidden_dim: int, output_dim: int) -> None:
    super(NonLinear, self).__init__()
    self.input_to_hidden = nn.Linear(input_dim, hidden_dim)
    self.non_linear_activation = nn.ReLU()
    self.hidden_to_hidden = nn.Linear(hidden_dim, hidden_dim // 2)
    self.hidden_to_output = nn.Linear(hidden_dim // 2, output_dim)
    # self.input_to_hidden = nn.Linear(input_dim, hidden_dim)
    # self.hidden_layer_1 = nn.Linear(hidden_dim, hidden_dim)
    # self.hidden_layer_2 = nn.Linear(hidden_dim, hidden_dim)
    # self.hidden_to_output = nn.Linear(hidden_dim, output_dim)
  def forward(self, input: torch.Tensor) -> torch.Tensor:
    hidden = self.input_to_hidden(input)
    hidden = self.non_linear_activation(hidden)
    hidden = self.hidden_to_hidden(hidden)
    hidden = self.non_linear_activation(hidden)
    output = self.hidden_to_output(hidden)
    return output
  
  def evaluate(self, model, test_loader, loss_function):
    model.eval()
    loss = 0
    with torch.no_grad():
            for idx, sample in enumerate(test_loader):
                output = model(sample['input'])
                target_output = sample['output']
                loss += loss_function(output, target_output.unsqueeze(1)).item()
    return loss/len(test_loader)