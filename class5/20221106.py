'''
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
'''
'''
from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4_HW1')
root.geometry('400x400+150+200')
mylabel=Label(root, text="點擊按鈕次數", fg='orange', font=('garamond','25','bold'))
mylabel.pack()
x=0
def clicked():
    global x
    x=x+1
    label1=Label(root,text=x)
    label1.pack()
mybutton=Button(root,text="Click me",command=clicked)
mybutton.pack(pady=20)




root.mainloop()
'''

# from tkinter import *
# root=Tk()
# root.title('class4_HW2')
# root.geometry('500x500')
# #side:牌面方向:TOP,BOTTOM,LEFT,RIGHT
# mybutton1=Button(root,text=('left'))
# mybutton2=Button(root,text=('right'))
# mybutton3=Button(root,text=('right1'))

# mybutton1
# root.mainloop()


#    fill:填滿所分配空間之方向:NONE,X,Y,BOTH
# from tkinter import *
# root=Tk()
# root.title('class4_HW2')
# root.geometry('500x500')
# mybutton1.pack(fill='x')
# mybutton2.pack(side='right',fill='y')
# root.mainloop()


#    expand:填滿容器:true/false
# from tkinter import *
# root=Tk()
# root.title('class4_HW2')
# root.geometry('500x500')
# mybutton1=Button(root,text='expand=0')
# mybutton1.pack(fill='both',expand=0)
# mybutton2=Button(root,text='expand=1')
# mybutton2.pack(fill='both',expand=1)

# root.mainloop()



# #     padx/pady:元件邊框與容器之距離(預設=0)
from tkinter import *
root=Tk()
root.title('class4_HW2')
root.geometry('500x500')
mybutton1=Button(root,text='left')
mybutton1.pack(side='left',padx=20)
mybutton2=Button(root,text='right')
mybutton2.pack(side='right',padx=30)

root.mainloop()


#     ipadx/ipady:元件內容(文字,圖像)與其邊框之距離(px,預設=0)
# from tkinter import *
# # root=Tk()
# # root.title('class4_HW2')
# # root.geometry('500x500')
# # mybutton1.pack(side='left',ipadx=30)
# # mybutton1=Button(root,text='left')
# # mybutton2.pack(side='right',ipadx=30)
# # mybutton2=Button(root,text='right')

# # root,mainloop()

