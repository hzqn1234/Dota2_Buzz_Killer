# from PIL import Image
import os
import sys

#check if its a compiled exe
if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
    filePath = os.path.join(sys._MEIPASS, "dota2.png")
    
#otherwise it must be a script 
else:
    scriptPath = os.path.realpath(os.path.dirname(sys.argv[0]))
    filePath = "dota2.png"
    
# Import Module
from tkinter import *
from tkinter.font import BOLD, Font
from tkinter import messagebox
 
# create root window
root = Tk()
root.eval('tk::PlaceWindow . center')

# set photo
# p1 = PhotoImage(file = 'dota2.png')
p1 = PhotoImage(file = filePath)
root.iconphoto(False, p1)

# root window title and dimension
root.title("Dota2 Pre-check")
root.geometry('400x200')

# adding a label to the root window
lbl = Label(root, text = "确定可以上分嘛?", font=Font(family='Arial',size=20, weight=BOLD))
lbl.place(relx=0.5, rely=0.3, anchor=CENTER)

# function to display text when
# button is clicked
n = 0
def clicked_yes():
    global n
    n=n+1
    threshold = 9
    if n < threshold:
        lbl.configure(text = "再想想：）确定可以上分嘛?")
    else:
        lbl.configure(text = "x"+"D"*(1+(n-threshold)%19))

def clicked_cross():
    global n
    n=n+1
    threshold = 9
    if n < threshold:
        lbl.configure(text = "回避问题就可以上分了嘛?")
    else:
        lbl.configure(text = "x"+"D"*(1+(n-threshold)%19))
        
# btn_yes
btn_yes = Button(root, text = "轻松上分！！！", fg = "grey", command=clicked_yes, font=Font(family='Arial',size=10))
btn_yes.place(relx=0.075, rely=0.725, anchor=SW)

# btn_no
btn_no = Button(root, text = "hmmm...那算了", fg = "green", command=root.destroy, font=Font(family='Arial',size=22, weight=BOLD))
btn_no.place(relx=0.95, rely=0.8, anchor=SE)

# close
def on_closing():
    clicked_cross()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Execute Tkinter
root.mainloop()