from tkinter import *
from tkinter import ttk

def Click(numbers):
    global operator
    operator=operator + str(numbers)
    text_Input.set(operator)

def Clear():
    global operator
    operator=""
    text_Input.set("")

def Equal():
    global operator
    sumup=str(eval(operator))
    text_Input.set(sumup)
    operator=sumup


cal=Tk()
cal.title("Calculator")
operator=""
text_Input=StringVar()

txtDisplay=Entry(cal,font=('arial',20,'bold'),textvariable=text_Input,bd=30,insertwidth=4,bg="white",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="7",command=lambda:Click(7),bg="white")
btn7.grid(row=1,column=0)

btn8=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="8",command=lambda:Click(8),bg="white")
btn8.grid(row=1,column=1)

btn9=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="9",command=lambda:Click(9),bg="white")
btn9.grid(row=1,column=2)

clear=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="C",command=lambda:Clear(),bg="blue")
clear.grid(row=1,column=3)

btn4=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="4",command=lambda:Click(4),bg="white")
btn4.grid(row=2,column=0)

btn5=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="5",command=lambda:Click(5),bg="white")
btn5.grid(row=2,column=1)

btn6=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="6",command=lambda:Click(6),bg="white")
btn6.grid(row=2,column=2)

Addiiont=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="+",command=lambda:Click('+'),bg="white")
Addiiont.grid(row=2,column=3)

btn1=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="1",command=lambda:Click(1),bg="white")
btn1.grid(row=3,column=0)

btn2=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="2",command=lambda:Click(2),bg="white")
btn2.grid(row=3,column=1)

btn3=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="3",command=lambda:Click(3),bg="white")
btn3.grid(row=3,column=2)

subraction=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="-",command=lambda:Click('-'),bg="white")
subraction.grid(row=3,column=3)

btn0=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="0",command=lambda:Click(0),bg="white")
btn0.grid(row=4,column=0)

multiply=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="*",command=lambda:Click('*'),bg="white")
multiply.grid(row=4,column=1)

division=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="/",command=lambda:Click('/'),bg="white")
division.grid(row=4,column=2)

equal=Button(cal,padx=16,bd=8,fg='black',font=('',20,'bold'),text="=",command=lambda:Equal(),bg="white")
equal.grid(row=4,column=3)


cal.mainloop()