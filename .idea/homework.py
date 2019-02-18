'''

a=int(input("enter the marks for 1st sub"))
b=int(input("enter the marks for 2nd sub"))
c=int(input("enter the marks for 3rd sub"))
d=int(input("enter marks for 4th sub"))
e=int(input("enter marks for 5th sub"))
list=[]
list.append(a)
list.append(b)
list.append(c)
list.append(d)
list.append(e)
print(sum(list))




input_string=input('enter the string')
check_string=input("the string to be counted")
print(input_string.count(check_string))



marks=int(input("enter the marks"))
if  marks>=40:
    print('passed')
else:
    print("failed")





birth_year=int(input("year"))
age= 2019-birth_year
if age>=18:
    print("eligible")
else:
    print("not elgible")





marks=input("enter marks")
if marks>=90 and marks<100:
    grade='A'
elif marks>=7- and marks<90:
    grade"b"



print("1 2 3 4 5")
'''


name=input("enter your name")
while name.isalpha()==False:
    print("enter your name agan")
    name=input("wrong input!!!")
print("welcome",name)



list=[10,2 ,4 ,6,7,15,23,45,9,20]
print("the list is",list)
print(max(list))
print(min(list))


'''input_string='i am a girl'
input_string=input_string.replace('girl','i nffbygh')
print(input_string.upper()) '''


str=input("enter the string")
new=input("new string u want to enter")
old=input('string you want to repace')
str=str.replace(old,new)
print(str.upper())


