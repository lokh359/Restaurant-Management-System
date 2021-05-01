from tkinter import*
import tkinter.messagebox
root1 = Tk()
root1.geometry("420x220+0+0")
root1.title("Login Page")

name_inp = StringVar()
password_inp = StringVar()



def enter():
	if name_inp.get() == "Mahender" and password_inp.get() == "1234":
		root1.destroy()
		import question
	else:
		tkinter.messagebox.showinfo('Error','enter valid username and pin')
		name_inp.set("")
		password_inp.set("")	

def destroy():
	root1.destroy()	


label = Label(root1, font = ('arial',20,'bold'), text ="Accountant Login", fg = "steel blue", bd = 10, anchor = 'w')
label.grid(row = 0)


label1 = Label(root1, font =('slant',10,'bold'),text="Username")
label2 = Label(root1, font =('slant',10,'bold'),text="Pin")
	
entry1 = Entry(root1, textvariable = name_inp)
entry2 = Entry(root1, textvariable = password_inp,show='*')

label1.grid(row=1, sticky=E)        
label2.grid(row=2,sticky=E)
entry1.grid(row=1,column=1)
entry2.grid(row=2,column=1)

enter_btn = Button(root1, text="Enter", command= enter)
enter_btn.grid(row=3, column=1)

exit_btn = Button(root1, padx= 1, text="Exit", command= destroy)
exit_btn.grid(row=3,column=2)

root1.mainloop()