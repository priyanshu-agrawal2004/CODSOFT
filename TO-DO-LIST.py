import tkinter
from tkinter import *
from tkinter import messagebox

main=Tk()
main.geometry("600x500")
main.title("TO-DO LIST")
main.config(bg="lightblue")
main.resizable(width=False, height=False)
#create frame
frame=Frame(main,height=15,width=20)
frame.pack(side=TOP)
#store tasks
lb=Listbox(frame,height=10,width=20, font=('Times', 22))
lb.pack(side=LEFT,fill=BOTH)
#srcollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
#scroller y axises
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
#insert tasks function
def add():
    task=l.get()
    if task!="":
        lb.insert(END,task)
    else:
        messagebox.showwarning("warring","Enter some tasks in textbox")
#delete tasks function        
def delete():
    task=l.get()
    if task!="":
        lb.delete(ANCHOR)
    else:
        messagebox.showwarning("warring","nothing else to delete")
#entry box
l=Entry(main,font=('times', 18))
l.pack(side=TOP,pady=10)
#create frame to store buttons
frame2=Frame(main)
frame2.pack(side=TOP)
b1=Button(frame2,text="Add",height=1,width=5,font=5,command=add)
b1.pack(side=LEFT)
b2=Button(frame2,text="Delete",height=1,width=5,font=5,command=delete)
b2.pack(side=LEFT)
b3=Button(frame2,text="Exit",height=1,width=5,font=5,command=exit)
b3.pack(side=LEFT)
#mainloop function to show 
main.mainloop()