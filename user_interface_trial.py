import tkinter
import user_test_2
import tkinter.messagebox
from tkinter import *

def trial():
    user_test_2.mainFrame()
    return

root = tkinter.Tk()

geomet = root.geometry('1000x500+0+0')

head_title = Label(root, font=('algerian', 28, 'bold'), text=" A.L.M.S Analytic Company ",bg = 'cyan', fg="steel blue", bd=15,
                   anchor='n')
head_title.pack(fill = X ,side = 'top')

photo = PhotoImage(file="credit_card.png")
label = Label(root, image=photo, anchor = 'n')
label.pack(side = 'top')

label_enter = Label(root, font = ('castellar',15), text = " Company user portal for fraud detection analysis ", bg = 'lightyellow', fg = 'purple',bd = 5, anchor = 'n')
label_enter.pack(expand = True, fill = X , side = 'top' )

label_user = Label(root , font = ('ariel',18), text = " Username",fg = 'black',anchor = 'nw')
entry_user = Entry(root)
label_user.pack()
entry_user.pack()

label_pass = Label(root , font = ('ariel',18), text = " Password",fg = 'black',anchor = 'ne')
entry_pass = Entry(root)
label_pass.pack()
entry_pass.pack()

but_1 = Button(root, text = " OK ", padx=20 , pady = 10, fg = 'green', anchor = 'sw',command = trial )
but_1.pack(side = 'left')

but_2 = Button(root, text=" Exit ", fg='red', padx=20, pady = 10, command= root.quit, anchor='se')
but_2.pack(side = 'right')


root.mainloop()
