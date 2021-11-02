"""
Author: Mai Duc Nhat Minh
Date: 17/09/2021
Problem:    Translate the following for loops to equivalent while loops:
a. for count in range(100):
 print(count)
b. for count in range(1, 101):
 print(count)
c. for count in range(100, 0, –1):
 print(count)
Solution:
    a.  count = 0
        while count < 100:
            print(count)
            count += 1
    b.  count = 1
        while 1 <= count <= 100:
            print(count)
            count += 1
    c.  count = 100
        while -1 <= count <= 100:
            print(count)
            count -= 1
    ....
"""
