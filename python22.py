#spinbox ile rgb 

import tkinter as tk
from tkinter.ttk import *

def renk():
    r = sr.get()
    g = sg.get()
    b = sb.get()
    #hex 16 lik koda dönüştürme
    rh = hex(int(r))
    gh = hex(int(g))
    bh = hex(int(b))
    color="#"+rh.replace("0x","")+gh.replace("0x","")+bh.replace("0x","")
    print(color)
    pencere.configure(bg=color)


pencere=tk.Tk()
pencere.geometry("300x300")


lred=Label(text="kırmızı")
lred.place(x=20,y=20)
sr=Spinbox(font="verdana 10 bold",from_=0,to=15,width=12,command=renk)
sr.place(x=80,y=20)

lgreen=Label(text="yeşil")
lgreen.place(x=20,y=80)
sg=Spinbox(font="verdana 10 bold",from_=0,to=15,width=12,command=renk)
sg.place(x=80,y=80)

lblue=Label(text="mavi")
lblue.place(x=20,y=140)
sb=Spinbox(font="verdana 10 bold",from_=0,to=15,width=12,command=renk)
sb.place(x=80,y=140)


pencere.mainloop()