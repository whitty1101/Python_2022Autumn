from tkinter import *
from datetime import*
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4_HW2')
root.geometry('400x400+150+200')
mylabel=Label(root, text="enter your birth date:\nInput format is yyyy.mm.dd", font=('Arial',16,'bold'))
mylabel.pack()
enterbox=Entry(root,width=30, font=('Arial',18,'bold'))
enterbox.pack()
def count():
    time_string=enterbox.get()
    t1=datetime.strptime(time_string, '%Y.%m.%d')
    t2=datetime.now()
    result=t2.year-t1.year
    label=Label(root,text='You are'+str(result)+'year old')
    label.pack()
mybutton=Button(root,text="Click me",command=count)
mybutton.pack(pady=20)


root.mainloop()