import tkinter
from tkinter import *

a=Tk()
a.title("CALCULATER")
a.geometry("362x250")
a.resizable(width=False,height=False)
a.configure(bg="lightgray")

exp=""
text=StringVar()
#functions
def enter(n1):
   global exp
   exp=exp+str(n1)
   text.set(exp)

def clear():
   text.set(exp)

def equal():
    global exp
    try:
        res=str(eval(exp))
        text.set(res)
        exp=""
    except:
       text.set("error")
       exp=""
#design calculater
e1=Entry(a,textvariable=text,width=20,font=("times",27))
e1.grid(row=0,column=0,columnspan=8)
b1=Button(a,text="7",width=7,font=20,command=lambda: enter(7))
b1.grid(row=2,column=0,columnspan=1)
b2=Button(a,text="8",width=7,font=20,command=lambda: enter(8))
b2.grid(row=2,column=1,columnspan=1)
b3=Button(a,text="9",width=7,font=20,command=lambda: enter(9))
b3.grid(row=2,column=2,columnspan=1)
b4=Button(a,text="4",width=7,font=20,command=lambda: enter(4))
b4.grid(row=3,column=0,columnspan=1)
b5=Button(a,text="5",width=7,font=20,command=lambda: enter(5))
b5.grid(row=3,column=1,columnspan=1)
b6=Button(a,text="6",width=7,font=20,command=lambda: enter(6))
b6.grid(row=3,column=2,columnspan=1)
b7=Button(a,text="1",width=7,font=20,command=lambda: enter(1))
b7.grid(row=4,column=0,columnspan=1)
b8=Button(a,text="2",width=7,font=20,command=lambda: enter(2))
b8.grid(row=4,column=1,columnspan=1)
b9=Button(a,text="3",width=7,font=20,command=lambda: enter(3))
b9.grid(row=4,column=2,columnspan=1)
b10=Button(a,text="0",width=7,font=20,command=lambda: enter(0))
b10.grid(row=5,column=1,columnspan=1)
#operations
b_add=Button(a,text="+",width=7,font=20,command=lambda: enter("+"))
b_add.grid(row=5,column=3,columnspan=1)
b_sub=Button(a,text="-",width=7,font=20,command=lambda: enter("-"))
b_sub.grid(row=4,column=3,columnspan=1)
b_div=Button(a,text="/",width=7,font=20,command=lambda: enter("/"))
b_div.grid(row=2,column=3,columnspan=1)
b_mul=Button(a,text="x",width=7,font=20,command=lambda: enter("*"))
b_mul.grid(row=3,column=3,columnspan=1)
b_eul=Button(a,text="=",width=7,font=20,command=lambda: equal())
b_eul.grid(row=5,column=2,columnspan=1)
b_cl=Button(a,text="Clear",width=24,font=20,command=lambda: clear())
b_cl.grid(row=1,column=0,columnspan=3)
b_exit=Button(a,text="Exit",command=exit,width=7,font=20)
b_exit.grid(row=1,column=3,columnspan=2)
b_dot=Button(a,text=".",width=7,font=20,command=lambda: enter("."))
b_dot.grid(row=5,column=0,columnspan=1)

a.mainloop()