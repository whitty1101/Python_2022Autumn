# #引入TKINTER MODULE
# from tkinter import *
# root=Tk()
# root.title('Class7')
# root.geometry('350x100')
# #加入frame框架
# frame=Frame(root)
# frame.pack()
# #家LABEL放在指定FRAME裡
# label=Label(frame,text='Hello World')
# label.pack()
# #執行主程式
# root.mainloop()




# #引入TKINTER MODULE
# from tkinter import *
# root=Tk()
# root.title('Class7')
# root.geometry('350x100')
# #加入frame框架
# frame=Frame(root)
# frame1=Frame(root,pady=5,padx=20,bg='lightblue')
# frame2=Frame(root,pady=20,padx=10,bg='pink')
# #放到FRAME1裡的LABEL
# label1=Label(frame1,text='hello',width=10)
# label1.pack()
# label2=Label(frame2,text='world',width=20)
# label2.pack()
# #先放FRAME2
# frame2.pack()
# frame1.pack()
# root.mainloop()




# #引入TKINTER MODULE
# from tkinter import *
# root=Tk()
# root.title('Class7')
# root.geometry('350x100')
# #加入frame框架
# frame=Frame(root)
# frame1=Frame(root,pady=5,padx=10,bg='green')
# frame2=Frame(root,pady=10,padx=2,bg='blue')
# #放到FRAME1裡的LABEL
# label1=Label(frame1,text='first',width=5)
# label1.pack()
# label2=Label(frame2,text='second',width=10)
# label2.pack()
# #先放FRAME2
# frame2.pack(side='right')
# frame1.pack(side='left')
# root.mainloop()



# #更新LABEL文字內容
# #方法1
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400')
# counter=0
# def clicked():
#     global counter
#     counter+=1
# mylabel['text']='click'+str(counter)
# mybutton=Button(root,text="Click me",command=clicked)
# mybutton.pack()
# mylabel=Label(root,text='clicked 0')
# mylabel.pack()
# root.mainloop()



# #更新LABEL文字內容
# #方法2
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400')
# counter=0
# def clicked():
#     global counter
#     counter+=1
#     mystringvar.set('click'+str(counter))
# mybutton=Button(root,text="button",command=clicked)
# mybutton.pack()
# mystringvar=StringVar()
# mystringvar.set('clicked0')
# mylabel=Label(root,textvariable=mystringvar)
# mylabel.pack()

# root.mainloop()



# #獲取LABEL文字內容
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400')
# mylabel=Label(root,text='Hello World')
# mylabel.pack()
# Label(root,text=mylabel['text']).pack
# root.mainloop()




# # 獲取LABEL文字內容
# from tkinter import *
# # #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400')
# mystringvar=StringVar()
# mystringvar.set('Hello World')
# mylabel=Label(root,textvariable=mystringvar)
# mylabel.pack()
# root.mainloop()



