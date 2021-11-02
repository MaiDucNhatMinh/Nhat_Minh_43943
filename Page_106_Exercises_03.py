"""
Author: Mai Duc Nhat Minh
Date: 25/09/2021
Problem:   Assume that the variable myString refers to a string. Write a code segment that
uses a loop to print the characters of the string in reverse order.
Solution:

    ....
"""
data = "myString"
for i in range(len(data),0 ,-1):
    print(i-1, data[i-1])
