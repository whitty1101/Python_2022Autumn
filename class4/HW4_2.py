from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4_HW2')
root.geometry('400x400+150+200')
mylabel=Label(root, text="enter your birth date", font=('Arial',16,'bold'))
mylabel.pack(pady=10)
mylabel2=Label(root, text="yyyy.mm.dd", font=('Arial',16,'bold'))
mylabel2.pack(pady=10)
def clicked():
    label1=Label(root,text=2022.0000 +str (e.get()))
    label1.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack()
e=Entry(root)
e.pack()

root.mainloop()