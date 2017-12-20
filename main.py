# -*- coding: utf-8 -*-
from random import randint

print("Enter a range for your roll:")
print("Min: ")
x = input()
print("Max: ")
y = input()

x = int(x)
y = int(y)

roll = randint(x, y)

print(roll)
