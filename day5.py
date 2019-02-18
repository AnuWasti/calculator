from tkinter import *
root=Tk()
root.title('Anu')
root.geometry("550x550")
root.config(background='yellow')
#label widget
title=Label(root,text="welcome",font=('Ariel',25),fg='blue',background='pink')
title.place(relx=0,rely=0)
root.resizable(1,1)
#entry widget
title2=Label(root,text="Enter Name",font=("Times New",10),fg='black',background='blue')
title2.pack(padx=10,pady=10)
name=Entry(root,width=15,font=('Ariel',15))
name.place(relx=0.1,rely=0.1)
title3=Label(root,text="Enter Age",font=('Times Roman',10),fg='black',background='blue')
title3.pack(padx=0.2,pady=0.2)
age=Entry(root,width=15,font=('',15))
age.place(relx=0.2,rely=(0.2))
root.mainloop()
