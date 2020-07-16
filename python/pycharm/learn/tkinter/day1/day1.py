import tkinter as tk
from tkinter import messagebox
class Application(tk.Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.createWidget()
    def createWidget(self):
        self.btn01= tk.Button(self,text='insert point',command=self.insertpoint)
        self.btnquit=tk.Button(self,text='insert end',command=self.insertend)
        self.e = tk.Entry(self,show="*")
        self.t = tk.Text(self,height=2)
        self.e.pack()
        self.t.pack()
        self.btn01.pack()
        self.btnquit.pack()

    def insertpoint(self):
        var=self.e.get()
        self.t.insert('insert',var)
    def insertend(self):
        var = self.e.get()
        self.t.insert("end",var)

if __name__=='__main__':
    root = tk.Tk()
    root.geometry("400x400+400+400")
    root.title("经典GUI程序")
    app = Application(master = root)
    root.mainloop()



