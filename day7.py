'''f=open('File.txt','w')
f.writelines('My name is \n Anu Wasti')
f.close()

f=open ("File.txt","r")
text=f.read()
print(text)()
#Or
with open ("file.text","r") as f:
    text=f.read()
    print(text)

f=open('File.txt','a')
f.writelines('\n  its my file')
f.close()



f12=open('File3.txt','w')
text=input('write to file...write quit to stop')
while text!='quit':
    f12.writelines(text+'\n')
    text=input()
print("done with writing")
f12.close()


try:
    a=int(input('enter no.'))
    b=int(input('enter 2nd no.'))
    div=a/b
    print('the result is',div)
except ZeroDivisionError:
    print('cant divide by zero')
except:
    print("some problem occured")

class LowAgeError(Exception):
    def __init__(self):
        super(LowAgeError,self).__init__("age should be greater than 18")

age=int(input('enter the age'))
if age<18:
    raise LowAgeError

else:
    print('accepted')


lst_com=[x for x in range(20)]
gen_exp=(x for x in range(20))
print('lst com>>>',lst_com)
print('gen exp>>>',gen_exp)
for x in gen_exp:

    print(x)


#even numbers
list=[x for x in range (2500) if x%2==0 ]
print(list)
'''
#prime numbers
list=[x for x in range (2500) if not [y for y in range(2,x) if x%y==0 ]]

print(list)


