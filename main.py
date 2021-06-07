from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_password():

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers+password_letters+password_symbols
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0,END)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def on_add_click():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showwarning("Oops!", "Please don't leave any fields empty!")
    elif len(password)<8:
        messagebox.showwarning("Password Too Short","Sorry your password is too short.\nIt must be at "
                                                    "least 8 characters")
    else:
        is_ok = messagebox.askokcancel("Save Password?", f"These are the details entered:\n"
                                                         f"Website: {website}\nEmail: {email}\n"
                                                         f"Password: {password}\n"
                                                         f"Is it ok to save?")

        if is_ok:
            with open("saved_passwords.txt", mode="a") as password_data:
                password_data.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1, columnspan=2, sticky="EW")

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username: ", bg="white")
email_label.grid(row=2, column=0)
password_label = Label(text="Password ", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW")
website_entry.focus()
email_entry = Entry()
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
email_entry.insert(0, "darrenhazan1@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1, sticky="EW")

# Buttons
password_button = Button(text="Generate Password", bg="white", command=generate_password)
password_button.grid(row=3, column=2, sticky="EW", padx=(10, 0))
add_button = Button(text="Add", bg="white", command=on_add_click)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

window.mainloop()
