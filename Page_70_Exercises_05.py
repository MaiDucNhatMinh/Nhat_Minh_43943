"""
Author: Mai Duc Nhat Minh
Date: 16/09/2021
Problem:  Assume that the variable teststring refers to a string. Write a loop that prints
each character in this string, followed by its ASCII value.
Solution:

    ....
"""
str1 = input("Enter your String : ")
for i in range(len(str1)):
    print("The ASCII Value of Character %c = %d" % (str1[i], ord(str1[i])))