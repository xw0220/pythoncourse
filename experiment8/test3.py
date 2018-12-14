import tkinter #只载入模块
#from tkinter import *

win=tkinter.Tk()
win.geometry("400x300")
win.title("白虎-710958")

label1=tkinter.Label(win,text="白虎-710958")
label1.pack()

my_button=tkinter.Button(win,text="我是一个小按钮")
my_button.pack()
def changelabel(event):
    current_text=label1.cget("text")
    if current_text=="白虎-710958":
        label1.config(text="我的新标签，我是白虎")
    else:
        label1.config(text="白虎-710958")
my_button.bind('<Button-1>',changelabel)

win.mainloop()
