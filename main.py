import os

import torch
# import torchviz

#
# def square(x):
#     return x ** 2
#
# def mul3(x):
#     return x * 3
#
# def mul_(x, y):
#     return x * y
#
# x = torch.tensor(3., requires_grad=True, dtype=torch.float)
# y = torch.tensor(2., requires_grad=True, dtype=torch.float)
#
# a = square(x)  # a = x^2
# b = mul3(a)  # b = 3a
# c = mul_(b, y)  # c = by
#
# # torchviz.make_dot(c, {"x":x, "y":y, "c":c}).view()
# c.backward()
# print(x.grad)
# print(y.grad)

x = torch.arange(4.0, requires_grad=True)
print(x)
y = 2 * torch.dot(x, x)
print(y)
y.backward()
print(x.grad)
