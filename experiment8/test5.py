import tkinter
win=tkinter.Tk()

can=tkinter.Canvas(win,bg='white',width=600,height=400)
can.pack()
can.create_rectangle(10,10,200,200)
#.gif   .png
myimage=tkinter.PhotoImage(file='./avatar.gif')
myimageid=can.create_image(300,200,image=myimage)

def moveimage(event):
    current_coods=can.coords(myimageid)
    print(current_coods)
    if event.keysym=='Up':
        can.coords(myimageid,current_coods[0],current_coods[1]-10)
    elif event.keysym=='Down':
        can.coords(myimageid, current_coods[0], current_coods[1] + 10)
    elif event.keysym=='Left':
        can.coords(myimageid, current_coods[0]-10, current_coods[1])
    elif event.keysym=="Right":
        can.coords(myimageid, current_coods[0] + 10, current_coods[1])
can.bind_all('<KeyPress>',moveimage)

win.mainloop()