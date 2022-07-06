from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(random.randint(6, 8))]
    password_list += [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(random.randint(2, 4))]
    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    website = website_entry.get()
    password = password_entry.get()
    email = email_entry.get()
    new_data = {
        website:
            {"email": email,
             "password": password},
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Empty fields", message="Please don't leave empty fields")
    else:
        enter_data = messagebox.askokcancel(title=website, message=f"Website {website} details:\n"
                                                                   f"email: {email}\n"
                                                                   f"Password: {password}\n"
                                                                   f"Do you want to save? ")
        if enter_data:
            try:
                with open("passwords.json", "r") as password_data:
                    data = json.load(password_data)
            except FileNotFoundError:
                with open("passwords.json", "w") as password_data:
                    json.dump(new_data, password_data, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as password_data:
                    json.dump(data, password_data, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sarunas@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

password_button = Button(text="Generate Password", command=password_generator, width=14)
password_button.grid(column=2, row=3)

add_password = Button(text="Add", command=save_info, width=33)
add_password.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", command=find_password, width=14)
search_button.grid(column=2, row=1)

window.mainloop()
