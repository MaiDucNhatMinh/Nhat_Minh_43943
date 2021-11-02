"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:  Write a loop that outputs the numbers in a list named salaries. The outputs should be
formatted in a column that is right-justified, with a field width of 12 and a precision of 2.
Solution:
    Output  13.580000
            2468.100000
            12345.68000
    ....
"""
salaries = [13.57911, 2468.10, 12345.6789]
for k in salaries:
    print("%12f" % round(k, 2))
