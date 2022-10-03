#引入TKINTER MODULE
from optparse import TitledHelpFormatter
from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('HELLO WHITE')
#                size   place
root.geometry('300x275+500+150')
#建立LABEL標籤
mylabel=Label(root, text="hello world", fg='orange',bg="white", font=('Arial',20,'bold'))
#加入視窗
mylabel.pack(pady=10)
def clicked():
    label1=Label(root,text=e.get())
    label1.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack()


e=Entry(root)
e.pack()


#執行主程式
root.mainloop()
