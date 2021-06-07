from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(bg="white", padx=50, pady=50)

logo_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200,height=200, bg="white",highlightthickness=0)
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

#Labels
website_label = Label(text="Website:",bg="white")
website_label.grid(row=1,column=0)
email_label = Label(text="Email/Username: ",bg="white")
email_label.grid(row=2,column=0)
password_label = Label(text="Password ",bg="white")
password_label.grid(row=3,column=0)

#Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1,columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2, column=1,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

#Buttons
password_button = Button(text="Generate Password", bg="white", width=20)
password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=40,bg="white")
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()
