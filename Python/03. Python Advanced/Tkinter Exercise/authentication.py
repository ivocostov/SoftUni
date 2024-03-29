from json import dump, loads
from canvas import root, frame
from tkinter import Button, Entry
from helpers import clean_screen



def get_users_data():
    info_data = []

    with open("DataBase/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads())  # s at end of loads stands for string reads as load s


def render_entry():
    register_btn = Button(
        root,
        text="Register",  # button text
        bg="green",  # background color
        fg="white",  # foreground(letters) color
        borderwidth=0,
        width=20,
        height=3,
        command=register,
    )

    login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        borderwidth=0,
        width=20,
        height=3,
        command=login,

    )

    frame.create_window(350, 260, window=register_btn)  # width and height of button
    frame.create_window(350, 320, window=login_btn)


def login():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(200, 50, window=username_box)
    frame.create_window(200, 50, window=password_box)

    login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        command=logging
    )

    frame.create_window(250, 150, window=login_btn)


def logging():
    if check_logging():
        pass
    else:
        frame.create_text(160, 200, text="Invalid username for password", fill="red")


def check_logging():
    info_data = get_users_data()

    user_username = username_box.get()
    user_password - password_box.get()

    for i in range(len(info_data)):
        username = info_data[i]["username"]
        password = info_data[i]["password"]

        if username == user_username and password == user_password:
            return True


def register():
    clean_screen()

    frame.create_text(100, 50, text="First name")  # creating inscriptions on screen
    frame.create_text(100, 100, text="Last name")
    frame.create_text(100, 150, text="Username")
    frame.create_text(100, 200, text="Password")

    frame.create_window(200, 50, window=first_name_box)  # creating spaces for entering data
    frame.create_window(200, 100, window=last_name_box)
    frame.create_window(200, 150, window=username_box)
    frame.create_window(200, 200, window=password_box)

    registration_btn = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        command=registration

    )

    frame.create_window(300, 250, window=registration_btn)


def registration():
    info_dict = {
        "first_name": first_name_box.get(),
        "last_name": last_name_box.get(),
        "username": username_box.get(),
        "password": get_password_hash(password_box.get())
    }


    if check_registration(info_dict):
        with open("DataBase/users_information.txt", "a") as users_file:
            dump(info_dict, users_file)  # if there is a s at end of dump stands for string



def check_registration(info):  # Checking if entered registration data is valid
    for el in info.values():
        if not el.strip():
            frame.create_text(
                300,
                300,
                text="We are missing some information",
                fill="red",
                tag="error"
            )

            return False

    frame.delete("error")  # deletes error tag if there is one


    info_data = get_users_data
    for record in info_data:
        if record["username"] == info["username"]:
            frame.create_text(
                300,
                300,
                text="User with this name already exists",
                tag="error"
            )

            return False
    frame.delete("error")  # deletes error tag if there is one


def check_if_loging_is_fulfilled(event):
    info = {
        "username": username_box.get(),
        "password": password_box.get(),
    }

    for el in info.values():
        if not el.strip():
            login_btn['state'] = "disabled"
            break
        else:
            login_btn["state"] = "normal"


first_name_box = Entry(root, bd=0)  # Input space for entering data
last_name_box = Entry(root, bd=0)  # Input space for entering data
username_box = Entry(root, bd=0)  # Input space for entering data
password_box = Entry(root, bd=0, show="*")  # Input space for entering data, password is shown as *

login_btn = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        command=logging
    )

login_btn["state"] = "disabled"


root.bind('<KeyRelease>', check_if_loging_is_fulfilled)  # Register button is availabel if everything is filled