from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4')
root.geometry('600x400+150+200')
mylabel=Label(root, text="name", fg='blue',bg="purple", font=('Arial',16,'bold'))
e=Entry(root)
e.pack()
def clicked():
    label1=Label(root,text=e.get()+'hi')
    label1.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack()
'''
mylabel=Label(root, text="2022.10.02", fg='blue',bg="purple", font=('Arial',16,'bold'))
mylabel.pack()
mylabel1=Label(root, text="sunday", fg='blue',bg="purple", font=('Arial',20,'italic'))
mylabel1.pack(pady=50)
def clicked():
    label2=Label(root,text='Harrison')
    label2.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack()
'''
root.mainloop()