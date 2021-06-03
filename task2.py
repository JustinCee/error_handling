# importing fo the tkinter modueles
from tkinter import *
from tkinter import messagebox

# Below is the configuration of the window
window = Tk()
window.title("Exception Handling")
window.geometry("400x200")
window.config(bg="Yellow")
# Below is the label and entry for the amount needed
top_label = Label(window, text="Please enter amount in your account", bg="yellow")
top_label.place(x=70, y=5)
input_label = Entry(window)
input_label.place(x=110, y=30)


# Below is the functions needed for the tkinter window to work
def qual():
    funds = input_label.get()
    try:
        funds = int(funds)
        if funds < 3000:
            messagebox.showerror("not enough funds", "Please deposit more funds.")
        else:
            messagebox.showinfo("Congratulations", "You qualify for the trip to Malaysia")
    except ValueError:
        messagebox.showerror("Error", "Please insert a valid number.")


def exit_program():
    window.destroy()


# Below is the buttons needed to call the function and to exit the program
qual_btn = Button(window, text="Check Qualification", fg="green", command=qual)
qual_btn.place(x=115, y=70)
exit_btn = Button(window, text="Exit", fg="Red", command=exit_program)
exit_btn.place(x=215, y=150)
window.mainloop()
