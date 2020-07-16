import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
class Application(tk.Frame):

    def __init__(self,master):
        super().__init__(master)
        #self.master = master
        self.pack()
        self.creatWidget()
    def creatWidget(self):
        self.lable1 = tk.Label(self,text= "确认",width=10,height=1,bg='black',fg='white')
        self.lable1.pack()
        self.btn02 = tk.Button(self,text="退出",command=root.destroy)
        self.btn02.pack()
        global photo    #定义在函数内部，如果不加global函数调用完后会被销毁
        image = Image.open("D:/Study/PythonCharm/PycharmProjects/learn/tkinter/photo/aaa.gif")
        photo = ImageTk.PhotoImage(image)
        self.lable2 =tk.Label(self,image=photo)
        self.lable2.pack()


root = tk.Tk()
root.geometry("400x400+400+400")
app = Application(master = root)
root.mainloop()
