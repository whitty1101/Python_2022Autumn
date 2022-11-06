from tkinter import *
#建立視窗FRAME
root=Tk()
#TITLE
root.title('class4_HW1')
root.geometry('400x400+150+200')
mybutton=Button(root,text="Click me")
mybutton1=Button(root,text="Click me")
mybutton2=Button(root,text="Click me")
mybutton.pack()
mybutton1.pack(side='left')
mybutton2.pack(side='bottom')

root.mainloop()






# from tkinter import *
# #建立視窗FRAME
# root=Tk()
# #TITLE
# root.title('class4_HW1')
# root.geometry('400x400+150+200')
# mybutton=Button(root,text="Click me")
# mybutton1=Button(root,text="Click me1")
# mybutton2=Button(root,text="Click me2")
# mybutton3=Button(root,text="Click me3")
# mybutton4=Button(root,text="Click me4")
# mybutton.pack(fill='x')
# mybutton1.pack(side='left', fill='y')
# mybutton2.pack(side='left')
# mybutton3.pack()
# mybutton4.pack(side='right')

# root.mainloop()