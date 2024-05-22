import customtkinter as ck
import customtkinter as tk
import mysql.connector
from BlurWindow.blurWindow import blur
from ctypes import windll
import re
import time

# import logging

def animate_text(text, label, delay=0.1, color="orange"):
    label.configure(text="", text_color=color)
    chars = list(text)
    for i in range(len(text)):
        label.configure(text="".join(chars[:i+1]))
        label.update()
        time.sleep(delay)

def Main_page():
    username = username_entry.get()
    password = password_entry.get()
    
    cursor.execute("SELECT nickname FROM Login_info WHERE username=%s AND password=%s", (username, password))
    result = cursor.fetchone()
    if result:
        nickname = result[0]
        login_page.withdraw()
        signup_page.withdraw()
        main_window = ck.CTkToplevel(login_page)
        main_window.geometry('800x600+400+100')
        main_window.wm_resizable(False, False)

        # Create a label widget to display the animated text
        label = ck.CTkLabel(main_window, font=("Arial", 24, "bold"), text_color="orange")
        label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Animate "Welcome " and the nickname on the same line
        animate_text("Welcome " + nickname+"..", label, delay=0.1, color="orange")

        # Wait for the main window to close
        main_window.wait_window()
    else:
        error_label = ck.CTkLabel(login_page, text="Invalid username or password")
        error_label.place(relx=0.82, rely=0.54, anchor=tk.CENTER)
        login_page.after(1000, error_label.place_forget)

def Signup_page():
    signup_page.deiconify()
    login_page.withdraw()

def Login_page():
    login_page.deiconify()
    signup_page.withdraw()

login_page=ck.CTk()

signup_page = ck.CTkToplevel(login_page)
signup_page.withdraw()

signup_page.wm_resizable(False,False)
signup_page.geometry('800x600+400+100')

ck.set_default_color_theme("green")
login_page.wm_resizable(False,False)
login_page.geometry('800x600+400+100')

sideframe=ck.CTkFrame(login_page,width=300,height=600,corner_radius=0)
sideframe.place(x=500,y=1)

label1 = ck.CTkLabel(sideframe,text='Welcome Back' , font=('Blackoak Std', 20, 'bold'))
label1.place(relx=0.52,rely=0.5,anchor=tk.CENTER)

username_entry = ck.CTkEntry(sideframe,width=220,placeholder_text="Username")
username_entry.place(relx=0.52,rely=0.58,anchor=tk.CENTER)

password_entry = ck.CTkEntry(sideframe,width=220,placeholder_text="Password",show="*")
password_entry.place(relx=0.52,rely=0.66,anchor=tk.CENTER)

signin_button = ck.CTkButton(sideframe,border_width=2,width=110,text='Sign In',command=Main_page)
signin_button.place(relx=0.34,rely=0.74,anchor=tk.CENTER)

label1 = ck.CTkLabel(sideframe,text="Don't have an account!" , font=('Blackoak Std', 12, 'bold'))
label1.place(relx=0.39,rely=0.80,anchor=tk.CENTER)

signup_button = ck.CTkButton(sideframe,border_width=2,width=110,text='Register',command=Signup_page)
signup_button.place(relx=0.72,rely=0.86,anchor=tk.CENTER)

#######################----------------------------------------------------------------------------------------------------------------

hWnd = windll.user32.GetForegroundWindow()
blur(hWnd)

username_error_label = None
email_error_label = None
nickname_error_label = None
phone_error_label = None
password_error_label = None

def validate_username(username):
    # Check if the username is between 4 and 20 characters long and contains only alphanumeric characters
    if len(username) < 4 or len(username) > 20 or not username.isalnum():
        return False
    return True

def validate_email(email):
    # Use a regular expression to check if the email is valid
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        return False
    return True

def validate_nickname(nickname):
    # Check if the nickname is between 2 and 20 characters long
    if len(nickname) < 2 or len(nickname) > 20:
        return False
    return True

def validate_phone(phone):
    # Check if the phone number is a valid 10-digit number
    if len(phone) != 10 or not phone.isdigit():
        return False
    return True

def validate_password(password):
    # Check if the password is between 6 and 20 characters long
    if len(password) < 6 or len(password) > 20:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def show_error_message(message, field):
    global username_error_label, email_error_label, nickname_error_label, phone_error_label, password_error_label

    if field == "username":
        if username_error_label is None:
            username_error_label = ck.CTkLabel(sideframe1, text="", text_color="red", wraplength=250)
            username_error_label.place(relx=0.52, rely=0.42, anchor=tk.CENTER)
        username_error_label.configure(text=message)
        signup_page.after(1000, username_error_label.place_forget) 
    elif field == "email":
        if email_error_label is None:
            email_error_label = ck.CTkLabel(sideframe1, text="", text_color="red", wraplength=250)
            email_error_label.place(relx=0.52, rely=0.5, anchor=tk.CENTER)
        email_error_label.configure(text=message)
        signup_page.after(1000, email_error_label.place_forget) 
    elif field == "nickname":
        if nickname_error_label is None:
            nickname_error_label = ck.CTkLabel(sideframe1, text="", text_color="red", wraplength=250)
            nickname_error_label.place(relx=0.52, rely=0.58, anchor=tk.CENTER)
        nickname_error_label.configure(text=message)
        signup_page.after(1000, nickname_error_label.place_forget)
    elif field == "phone":
        if phone_error_label is None:
            phone_error_label = ck.CTkLabel(sideframe1, text="", text_color="red", wraplength=250)
            phone_error_label.place(relx=0.52, rely=0.66, anchor=tk.CENTER)
        phone_error_label.configure(text=message)
        signup_page.after(1000, phone_error_label.place_forget)
    elif field == "password":
        if password_error_label is None:
            password_error_label = ck.CTkLabel(sideframe1, text="", text_color="red", wraplength=250)
            password_error_label.place(relx=0.52, rely=0.74, anchor=tk.CENTER)
        password_error_label.configure(text=message)
        signup_page.after(1000, password_error_label.place_forget) 

def show_success_message(message):
    success_label = ck.CTkLabel(signup_page, text=message, text_color="green")
    success_label.place(relx=0.82, rely=0.78, anchor=tk.CENTER)
    signup_page.after(3000, success_label.destroy)

def register_user():
    username = signup_username_entry.get()
    email = email_entry.get()
    nickname = nickname_entry.get()
    phoneno = phoneno_entry.get()
    password = signup_password_entry.get()

    # Validate the input fields
    if not validate_username(username):
        show_error_message("Invalid username.", "username")
        return
    if not validate_email(email):
        show_error_message("Invalid email address.", "email")
        return
    if not validate_nickname(nickname):
        show_error_message("Invalid nickname.", "nickname")
        return
    if not validate_phone(phoneno):
        show_error_message("Invalid phone number.", "phone")
        return
    if not validate_password(password):
        show_error_message("Invalid password.", "password")
        return

    # If all input fields are valid, insert the data into the database
    cursor.execute("INSERT INTO Login_info (username, email, nickname, phoneno, password) VALUES (%s, %s, %s, %s, %s)",
                   (username, email, nickname, phoneno, password))
    conn.commit()

    # Clear the input fields
    signup_username_entry.delete(0, "end")
    email_entry.delete(0, "end")
    nickname_entry.delete(0, "end")
    phoneno_entry.delete(0, "end")
    signup_password_entry.delete(0, "end")

    show_success_message("Registration successful!")
sideframe1=ck.CTkFrame(signup_page,width=300,height=600,corner_radius=0)
sideframe1.place(x=500,y=1)

labels = ck.CTkLabel(sideframe1,text='Sign Up' , font=('Blackoak Std', 20, 'bold'))
labels.place(relx=0.51,rely=0.29,anchor=tk.CENTER)

signup_username_entry = ck.CTkEntry(sideframe1,width=220,placeholder_text="Username")
signup_username_entry.place(relx=0.52,rely=0.38,anchor=tk.CENTER)

email_entry = ck.CTkEntry(sideframe1,width=220,placeholder_text="Email")
email_entry.place(relx=0.52,rely=0.46,anchor=tk.CENTER)

nickname_entry = ck.CTkEntry(sideframe1,width=220,placeholder_text="Nickname")
nickname_entry.place(relx=0.52,rely=0.54,anchor=tk.CENTER)
    
phoneno_entry = ck.CTkEntry(sideframe1,width=220,placeholder_text="Phone")
phoneno_entry.place(relx=0.52,rely=0.62,anchor=tk.CENTER)

signup_password_entry = ck.CTkEntry(sideframe1,width=220,placeholder_text="Password",show="*")
signup_password_entry.place(relx=0.52,rely=0.7,anchor=tk.CENTER)

register_button = ck.CTkButton(sideframe1,text="Sign Up",width=110,border_width=2,command=register_user)
register_button.place(relx=0.32,rely=0.86,anchor=tk.CENTER)

register_button = ck.CTkButton(sideframe1,text="Sign In",width=110,border_width=2,command=Login_page)
register_button.place(relx=0.72,rely=0.86,anchor=tk.CENTER)

def clear_error_labels(event):
    global username_error_label, email_error_label, nickname_error_label, phone_error_label, password_error_label

    if username_error_label:
        username_error_label.configure(text="")
    if email_error_label:
        email_error_label.configure(text="")
    if nickname_error_label:
        nickname_error_label.configure(text="")
    if phone_error_label:
        phone_error_label.configure(text="")
    if password_error_label:
        password_error_label.configure(text="")

signup_username_entry.bind("<Key>", clear_error_labels)
email_entry.bind("<Key>", clear_error_labels)
nickname_entry.bind("<Key>", clear_error_labels)
phoneno_entry.bind("<Key>", clear_error_labels)
signup_password_entry.bind("<Key>", clear_error_labels)

conn = mysql.connector.connect(host="localhost",user="Ather",passwd="webee312@!",database="Personal")
cursor = conn.cursor()

conn.commit()

login_page.mainloop()