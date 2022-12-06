from tkinter import *
root=Tk()
root.title('class6')
root.geometry('300x200')


kube_shop=Label(root,text='kube_shop').grid(row=0,column=1,columnspan=2)
沙發組=Label(root,text='沙發組').grid(row=1,column=0)
money=Label(root,text='$1200').grid(row=1,column=1)
zero=Label(root,text='0').grid(row=2,column=1)
minus=Button(root,text='-').grid(row=2,column=2,columnspan=2)
x=0
def clicked():
    global x
    x=x+1
    label1=Label(root,text=x)
    label1.pack()
add=Button(root,text='+',command=clicked).grid(row=2,column=0,columnspan=2)
root.mainloop()