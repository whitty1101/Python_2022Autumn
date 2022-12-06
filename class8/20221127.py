# #更改BUTTON內容  WAY1
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# mylabel=Label(root, text="點擊按鈕次數", fg='orange', font=('garamond','25','bold'))
# mylabel.pack()
# x=0
# def clicked():
#     global x
#     x=x+1
#     mystringvar.set('click'+str(x))
# mystringvar=StringVar()
# mystringvar.set("click")
# mybutton=Button(root,textvariable=mystringvar,command=clicked)
# mybutton.pack(pady=20)
# root.mainloop()


# #更改BUTTON內容   WAY2
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# mylabel=Label(root, text="點擊按鈕次數", fg='orange', font=('garamond','25','bold'))
# mylabel.pack()
# x=0
# def clicked():
#     global x
#     x=x+1
#     mybutton['text']='click'+str(x)
# mybutton=Button(root,text='click me',command=clicked)
# mybutton.pack(pady=20)
# root.mainloop()



# #獲取BUTTON內容  WAY1
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# mybutton=Button(root,text='hello world')
# mybutton.pack(pady=20)
# Label(root,text=mybutton['text']).pack()
# root.mainloop()



# #獲取BUTTON內容  WAY1
# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# mystringvar=StringVar()
# mystringvar.set('hello world')
# mybutton=Button(root,textvariable=mystringvar)
# mybutton.pack()
# Label(root,text=mystringvar.get()).pack()
# root.mainloop()




# from tkinter import *
# from PIL import Image, ImageTk
# root=Tk()
# root.title('hi')
# root.geometry('400x400+150+200')
# #開啟圖片
# img=Image.open("C:/Users/User/Documents/python_2022Autumn/class8/corgi1.jpg")
# #更改圖片大小
# resized_image=img.resize((100,100))
# #轉換為TK圖片物件
# tk_img=ImageTk.PhotoImage(resized_image)

# label=Label(root,image=tk_img)
# label.pack()
# root.mainloop()




# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import messagebox
# messagebox.showinfo('showinfo','message test')


# from tkinter import *
# from PIL import Image, ImageTk
# from tkinter import messagebox
# messagebox.askquestion('askquestion','Is it sunday')



from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
result=messagebox.askquestion('askquestion','Is it sunday')
print('User click'+result)