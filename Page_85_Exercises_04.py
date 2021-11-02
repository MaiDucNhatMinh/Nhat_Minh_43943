"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:   Assume that the variables x and y refer to strings. Write a code segment that prints
these strings in alphabetical order. You should assume that they are not equal.
Solution:

    ....
"""
x = 65
y = 97
for num in range(x, 90, 1):
    x = chr(num)
    print(x)
for count in range(y, 123, 1):
    y = chr(count)
    print(y)
