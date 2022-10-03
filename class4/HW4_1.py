from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4_HW1')
root.geometry('400x400+150+200')
mylabel=Label(root, text="點擊按鈕次數", fg='orange', font=('Courier',18,'bold'))
x=0
x=x+1
def clicked():
    label1=Label(root,text=x)
    label1.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack()




root.mainloop()

