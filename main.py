from ast import Return
from email.mime import image
from tkinter import *
from tkinter import filedialog
import tkinter


# initialise the tkinter
root = Tk()

root.geometry("600x600")
root.title("Notepad--")
root.config(bg="white")
root.resizable(False,False)


entry = Text(root,height='33',width='77',wrap=WORD,bg='#add8e6')
entry.place(x=0,y=60)

def open_file():
    file = filedialog.askopenfile(mode='r',filetypes=[('text files',"*txt")])
    if file is not None:
        content = file.read()
    entry.insert(INSERT,content)

def save_file():
    open_file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    text =str(entry.get(1.0,END))
    open_file.write(text)
    open_file.close()




b1 =Button(root,width='20',height='2',bg='#add8e6',text='Open',command=open_file).place(x=100,y=5)
b2 =Button(root,width='20',height='2',bg='#add8e6',text='Save File',command=save_file).place(x=300,y=5)






root.mainloop()





