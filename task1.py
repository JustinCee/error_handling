# importing the tkinter module
from tkinter import *
from tkinter import messagebox

# below is the configuration of the tkinter window
root = Tk()
root.title("Authentication")
root.geometry("300x300")
root.config(bg="yellow")
# below is the labels and entry fields for the username and password
top_label = Label(root, text="Please Enter Login Details Below", bg="Yellow")
top_label.place(x=50, y=5)
input_user = Label(root, text="Username", bg="yellow")
input_user.place(x=115, y=70)
user_entry = Entry(root)
user_entry.place(x=70, y=100)

input_pass = Label(root, text="Password", bg="Yellow")
input_pass.place(x=115, y=150)
pass_entry = Entry(root)
pass_entry.place(x=70, y=180)


# below is the functions needed for the login details and to clear and exit the program
def check():
    username = ["justin", "abdullah", "jason", "jesse"]
    passwords = ["1111", "2222", "3333", "4444"]
    found = False
    for x1 in range(len(username)):
        if user_entry.get() == username[x1] and pass_entry.get() == passwords[x1]:
            found = True
        if found == True:
            messagebox.showinfo("STATUS", "Access granted")
        root.destroy()
        import task2
    else:
        messagebox.showinfo("ERROR INFO", "Access denied")


def clear():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)


def exit_program():
    root.destroy()


# below is the placement of all the buttons needed for the program
login_btn = Button(root, text="Login", fg="green", command=check)
login_btn.place(x=10, y=250)
clear_btn = Button(root, text="Clear", command=clear)
clear_btn.place(x=110, y=250)
exit_btn = Button(root, text="Exit", fg="Red", command=exit_program)
exit_btn.place(x=220, y=250)

root.mainloop()
