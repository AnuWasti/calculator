'''
#write a program to find the area of a circle.The value of te radius must be entered by the user.
import math
r=float(input("enter the value of radius:"))
pi=3.14
area=pi*r*r
print('area is',area)


#write a function pow(a,b).The function should return the value a raised to power of b.
#(a^b)
a=int(input("enter value of a"))
b=int(input("enter power to be calculated"))
ans=a**b
print(ans)


#program for armstrong e.g.=371(3^3+7^3+1^3=371)

num=int(input("enter a number"))
a=num
while True:
    r=a%10
    a=a/10
    A=r**3
    r=r+1
A=sum +A
if(num==A):
    print("armstrong")
else:
    print("not")



import os
print("my current working directory:",os.getcwd())


import datetime as dt
import month

print(dt.date.today)
print(dt.month.today)
print(dt._datemonth.today)
'''


import math
a=int(input("enter a number"))
#b=int(input("enter 2nd number"))

print("Bin:",math.bin(a))
'''




