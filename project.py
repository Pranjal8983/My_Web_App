from tkinter import *
root = Tk() 
root.geometry("500x300")

Label(root, text="Library Login Form", font="arial 17 bold").grid(row=0, column=4)
name = Label(root, text="name")
phone = Label(root, text="phone")
mailID = Label(root, text="mailID")
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
mailID.grid(row=3, column=2)
root.mainloop()
