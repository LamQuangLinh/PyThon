from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH
from tkinter.ttk import Frame, Style

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.initUI()
    
    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        Style().configure("TFrame", background="#333")

        bard = Image.open("chuvit.jpg")
        bard = bard.resize((100, 100))
        bardejov = ImageTk.PhotoImage(bard)
        labell = Label(self, image=bardejov)
        labell.image = bardejov
        labell.place(x=20, y =20)

        rot = Image.open("kaito.jpg")
        rot = rot.resize((100, 100))
        rotunda = ImageTk.PhotoImage(rot)
        labell = Label(self, image=rotunda)
        labell.image = rotunda
        labell.place(x=40, y =160)

        minc = Image.open("conan2.jpg")
        minc = minc.resize((100, 100))
        mincol = ImageTk.PhotoImage(minc)
        labell = Label(self, image=mincol)
        labell.image = mincol
        labell.place(x=170, y =50)

root = Tk()
root.geometry("300x280+300+300")
app = Example(root)
root.mainloop()