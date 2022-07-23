# 87. Write a Program to solve the given equation assuming that a,b,c,m,n,o are constants:
# ax + by = c
# mx + ny = o
# # By solving the equation, we get:

a, b, c, m, n, o = 5, 9, 4, 7, 9, 4
temp = a*n - b*m
if n != 0:
   x = (c*n - b*o) / temp`
   y = (a*o - m*c) / temp
   print(str(x), str(y))
#
# n=5
# num=1
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(num,end=" ")
#         num=num+1
#     print()

# low=int(input("Enter low num"))
# up=int(input("Enter up num"))
# for n in range(low,up):
#     if n>1:
#         for i in range(2,n):
#             if (n%i)==0:
#                 break
#         else:
#             print(n)

# n=5
# for i in range(0,n+1,1):
#     print('* ' * i)

# import mysql.connector
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="yourusername",
#   password="yourpassword"
# )
#
# print(mydb)


# import keyword
# keyw=keyword.kwlist
# for k in keyw:
#     print(k)
# s = "if"
#
#
# # using iskeyword() function to check
# print(s,"is a keyword in Python:",
#       keyword.iskeyword(s))
#
#
# import sys
# print("A")
# print(sys.path)
# sys.exit()
# print("B")


# import functools
# print("The contents of the random library are::")
# print(dir(functools))
#
#
# import math
# print(dir(math))








