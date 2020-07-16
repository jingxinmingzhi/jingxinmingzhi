import tkinter as tk
from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
# from PIL import Image, ImageTK
class Application(tk.Frame):
    def __init__(self,master):
        self.master=master
        super().__init__(master)
        self.creatWidget()
    def creatWidget(self):
        self.btn01 = tk.Button(text="想",command=self.method1)
        self.btn02 = tk.Button(text="不想", command=self.method2)
        self.lable1=tk.Label(text="你想一夜暴富吗")

        image=Image.open("D:/Study/PythonCharm/PycharmProjects/learn/tkinter/photo/love.gif")
        global photo
        photo = ImageTk.PhotoImage(image)
        self.lable2=tk.Label(image=photo)
        self.btn01.pack()
        self.btn02.pack()
        self.lable1.pack()
        self.lable2.pack()
        pass
    def method1(self):
        messagebox.showinfo("祝你梦想成真")
        pass
    def method2(self):
        messagebox.showinfo("没有梦想和咸鱼有什么区别")
        pass
if __name__=='__main__':
    root = Tk()
    root.title("SAIC")
    root.geometry("400x400+400+400")
    app = Application(master=root)
    root.mainloop()
