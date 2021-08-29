from tkinter import *
import bcrypt


def validate(password):
    hash = b'$2b$12$RW7C4ErcHRpjUdU8KtWfu.xtnQz/.XAWlehfGZFIjteQNCOUpnlNe'
    password = bytes(password, encoding='utf-8')
    if bcrypt.checkpw(password, hash):
        print("Login Successful")
    else:
        print("Invalid Password")


root = Tk()
root.geometry("400x400")

password_entry = Entry(root)
password_entry.pack()

button = Button(text="Validate",
                command=lambda: validate(password_entry.get()))
button.pack()

root.mainloop()
