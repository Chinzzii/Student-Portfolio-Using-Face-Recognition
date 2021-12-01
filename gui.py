
from tkinter import *

root = Tk()
root.title('GUI')
root.geometry('200x500')

def func1():
    #label2 = Label(root,text = 'Pluck pluck').pack()
    pass

def deluser() : pass
def useradd(): pass

label1 = Label(root,text = 'Helo').grid(row = 0,column = 0 )
button1 = Button(root,text = 'Click Here',command = func1, width= 20 ).grid(row = 1,column = 0 )
buttonAddUser = Button(root,text = 'Add User' , command = useradd , width = 20).grid(row = 2,column = 0 )
buttonDeleteUser = Button(root , text = 'Delete User' , command = deluser , width = 20 ).grid(row = 3 , column = 0)
buttonTryFR = Button(root , text = 'Try Face Recognition' , command = deluser , width = 20 ).grid(row = 4 , column = 0)

root.mainloop()