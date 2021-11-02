"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:   Construct truth tables for the following Boolean expressions:
a. not (A or B)
b. not A and not B
Solution:

    ....
"""
a = int(input("nhập a:"))
b = int(input("nhập b:"))
A = not(a or b)
print(A)
B = not a and not b
print(B)