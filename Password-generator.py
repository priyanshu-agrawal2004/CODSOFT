import tkinter
from tkinter import *
from tkinter import messagebox
import string,random

a=Tk()
a.geometry("700x400")
a.resizable(FALSE,FALSE)
a.title("Password Generator")

def password():
    try:
        e2.delete(0,END)
        length=int(e1.get())
        if length<=0:
             messagebox.showwarning("warning","please enter correct input")
        else:
            text=string.ascii_letters+string.digits+string.punctuation
            password="\n".join(random.choice(text) for i in range(length))
            e2.insert(0,password)
            
    except:
        messagebox.showwarning("warning","please enter only integer value")

def clear():
    e1.delete(0,END)
    e2.delete(0,END)

l1=Label(a,text="Enter length of password",height=2,width=20,font=("times",20))
l1.grid(row=1,column=1)

e1=Entry(a,font=("times",20))
e1.grid(row=1,column=2)

b_pass=Button(a,text="Generate Password",height=2,width=20,font=("times",15),command=password)
b_pass.grid(row=2,column=2)

l2=Label(a,text="Your password is:",height=2,width=20,font=("times",20))
l2.grid(row=3,column=1)

e2=Entry(a,font=("times",20))
e2.grid(row=3,column=2)

b_cl=Button(a,text="Clear",height=2,width=20,font=("times",15),command=clear)
b_cl.grid(row=4,column=2)

a.mainloop()