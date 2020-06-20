import tkinter as tk

def topla():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1+s2)

def cıkar():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1-s2)

def carp():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1*s2)

def böl():
    s1=int(sayi1.get())
    s2=int(sayi2.get())
    sonuc['text']=str(s1/s2)

pencere=tk.Tk()
pencere.geometry("500x500")

sayi1=tk.Entry(width=10)
sayi1.place(x=20,y=20)

sayi2=tk.Entry(width=10)
sayi2.place(x=100,y=20)

sonuc=tk.Label(text="sonuç",bg="yellow",font="verdana 15 bold")
sonuc.place(x=180,y=20)

btopla=tk.Button(text="+",bg="green",font="verdana 15 bold",command=topla).place(x=20,y=50)

bcıkar=tk.Button(text="-",bg="green",font="verdana 15 bold",command=cıkar).place(x=100,y=50)

bcarp=tk.Button(text="*",bg="blue",font="verdana 15 bold",command=carp).place(x=180,y=50)

bböl=tk.Button(text="/",bg="orange",font="verdana 15 bold",command=böl).place(x=260,y=50)



pencere.mainloop()