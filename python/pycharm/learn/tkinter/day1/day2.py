import tkinter as tk
from tkinter import messagebox


def insertpoint():
    var = e.get()
    t.insert('insert', var)


def insertend():
    var = e.get()
    t.insert("end", var)


root = tk.Tk()
root.geometry("400x400+400+400")
root.title("无架构的GUI程序")

btn01 = tk.Button(text='insert point', command=insertpoint)
btnquit = tk.Button(root, text='insert end', command=insertend)
e = tk.Entry(root, show="*")
t = tk.Text(root, height=2)
e.pack()
t.pack()
btn01.pack()
btnquit.pack()

root.mainloop()
