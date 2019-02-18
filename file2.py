'''from file1 import *
import file1
print(name)
name='sweta'
print(name)
print(age)
print(place)



import datetime as  dt
import time

print(dt.date.today())
print('Formatted time:',time.asctime())


import webbrowser
a=input ("search video")
print("opening Browser")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)


import os
print('My current working directory:',os.getcwd())

import math
num=(int(input('enter a number')))
print('Factorial:',math.factorial(num))


from termcolor import colored

print(colored('Hii','white','on_grey'),colored('Anu','yellow','on_white'))

text=colored('color doesntlook Nice!!!',"blue",attrs=['reverse','blink'])

print(text)

'''

def fun (a,b):
    print('the values are')
    fun(2,3)
