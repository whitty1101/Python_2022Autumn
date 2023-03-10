# from tkinter import *
# from tkinter import messagebox
# root=Tk()
# root.title('hi')
# root.geometry('400x400+150+200')
# #宣告文字變數
# val=StringVar()
# def clicked1():
#     #以下為點選RADIObtn1後要執行的結果
#     label['textvariable']=val
#     label['fg']='Black'
# def clicked2():
#     #以下為點選RADIObtn2後要執行的結果
#     label['textvariable']=val
#     label['fg']='Green'
# def clicked3():
#     #以下為點選RADIObtn3後要執行的結果
#     label['textvariable']=val
#     label['fg']='Red'
# #放入第一個單選按鈕
# radiobtn1=Radiobutton(root,text='Black', fg='black', variable=val, value='Black',command=clicked1)
# radiobtn1.pack()
# #指定選取第一個單選按鈕
# radiobtn1.select()
# #放入第二個單選按鈕
# radiobtn2=Radiobutton(root,text='Green', fg='green',variable=val, value='Green',command=clicked2)
# radiobtn2.pack()
# radiobtn3=Radiobutton(root,text='Red', fg='red',variable=val, value='RED',command=clicked3)
# radiobtn3.pack()
# label=Label(root,textvariable=val,font=('Arial',30))
# label.pack()
# root.mainloop()




# from tkinter import *
# root=Tk()
# root.title('hi')
# root.geometry('400x400+150+200')
# #典籍BUTTON跳出NEW WINDOWS
# def createNewWindow():
#     #建立NEW WINDOWS
#     newWindows=Toplevel(root)
#     #建立LABEL在NEW WINDOWS
#     mylabel=Label(newWindows,text='new window')
#     mylabel.pack()
#     #建立QUIT BUTTON在NEW WINDOWS李
#     destroybutton=Button(newWindows,text='QUIT',command=newWindows.destroy)
#     destroybutton.pack()
#     #建立HIDE BUTTON在NEW WINDOWS李
#     hidebutton=Button(newWindows,text='hide',command=root.iconify)
#     hidebutton.pack()
#     #建立SHOW BUTTON在NEW WINDOWS李
#     showbutton=Button(newWindows,text='show',command=root.deiconify)
#     showbutton.pack()
#     #建立withdraw BUTTON在NEW WINDOWS李
#     withdrawbutton=Button(newWindows,text='Withdraw Main Window',command=root.withdraw)
#     withdrawbutton.pack()
#     #建立KILL BUTTON 在NEW WINDOWS李
#     killmainbutton=Button(newWindows,text='quit Main Window',command=root.destroy)
#     killmainbutton.pack()
#     newWindows.mainloop()
# #典籍BUTTON產生NEW WINDOWS
# createNewWindowbtn=Button(root,text='click',command=createNewWindow)
# createNewWindowbtn.pack()
# root.mainloop()





# #可變參數
# def funtion(n,*args):
#     print(n)
#     print(args)
# #呼叫執行FUNTION並多給(>2個)參數值傳入該FUNTION
# #除了1為變數n其餘都是*args的數值
# funtion(1,2,3,4,5,6,7)




def funtion(*args,**kwargs):
    print(kwargs)
    print(args)
#呼叫直型FUNTION並給多的(>2個)參數值傳入該FUNTION
#前四個值為*args可變參數後兩個值為**kwargs關鍵字可變參數
funtion(1,2,3,4,num1=5,num2=10)

