from torch import Tensor, exp, max
import torch.nn as nn

data = Tensor([1, 2, 3])


class MySoftmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        c = max(x, dim=0)
        x_exp = exp(x - c.values)
        total = x_exp.sum(0, keepdim=True)
        return x_exp / total


my_softmax = MySoftmax()
print(my_softmax(data))
