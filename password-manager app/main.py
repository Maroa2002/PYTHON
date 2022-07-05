from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for letter in range(randint(8, 10))]
    random_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    random_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = [*random_symbols, *random_letters, *random_numbers]
    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_data = website_entry.get()
    email_data = email_entry.get()
    password_data = password_entry.get()

    new_data = {
        website_data: {
            "email": email_data,
            "password": password_data
        }
    }

    if len(website_data) == 0 or len(password_data) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any field empty!")
    else:
        # is_ok = messagebox.askokcancel(
        #     title="Confirmation",
        #     message=f"These are the details you entered: \nWebsite:{website_data} \nEmail:{email_data} \nPassword:"
        #             f"{password_data} \nIs it okay to save?")
        # if is_ok:
        #     with open("data.txt", mode="a") as data:
        #         data.write(f"\n{website_data} | {email_data} | {password_data}")
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Update old data with new data
            data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD----------------- #!


def find_password():
    website_data = website_entry.get()
    try:
        with open("data.json", "r") as data_file:
            # Reading old data
            data_dict = json.load(data_file)
            # print(data_dict)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No data file found")
    else:
        if len(website_data) == 0:
            messagebox.showerror(title="Error", message="Please fill in the website entry!")

        elif website_data in data_dict:
            messagebox.showinfo(title=f"{website_data}", message=f"Email: {data_dict[website_data]['email']} \nPassword: "
                                                                 f"{data_dict[website_data]['password']}")
        elif website_data not in data_dict:
            messagebox.showerror(title="Error", message=f"No details for {website_data} exist")


# ---------------------------- UI SETUP ------------------------------- #![](logo.png)


window = Tk()
window.title("Password manager")
window.config(padx=60, pady=60)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

# labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# entries
website_entry = Entry(width=30)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_entry = Entry(width=50)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "matikomaroa12@gmail.com")


password_entry = Entry(width=30)
password_entry.grid(row=3, column=1)


# Buttons
search_btn = Button(text="Search", width=16, bg="white", command=find_password)
search_btn.grid(row=1, column=2)

generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(row=3, column=2)

add_button = Button(text="Add", width=47, bg="white", command=save, highlightthickness=0)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()
