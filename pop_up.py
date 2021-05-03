from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import random
import images

def on_closing(window):
    window.destroy()
    for i in range(random.randrange(3)+1):
        openNewWindow()

def openNewWindow():
    newWindow = Toplevel(master)
    newWindow.title("CLICK HERE")
    newWindow.protocol("WM_DELETE_WINDOW", lambda arg=newWindow: on_closing(arg))
    num = random.randrange(21)
    img = ImageTk.PhotoImage(Image.open("./images/{}.png".format(num)))
    panel = Label(newWindow, image = img)
    panel.pack(side = "bottom", fill = "both", expand = "yes")
    panel.image = img
    x = random.randrange(panel.winfo_reqwidth())
    y = random.randrange(panel.winfo_reqheight()) 
    newWindow.geometry('%dx%d+%d+%d' % (panel.winfo_reqwidth(), panel.winfo_reqheight(), x, y))

if __name__ == "__main__":
    master = Tk()
    master.withdraw()
    openNewWindow()
    mainloop()