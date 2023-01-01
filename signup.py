# Mickael Dias
# Password generator with simple GUI, tkinter, ttkbootstrap
# ttkbootstrap: https://ttkbootstrap.readthedocs.io/en/latest/
# Icons from: https://icon-icons.com/ | https://icons8.com/
# /////////////////////////////////////////////////////////


# Import modules
from tkinter import *
from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from PIL import ImageTk, Image
from random import choice
import string


class Window(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)

        # Image for title signup
        self.icon_title = ImageTk.PhotoImage(Image.open("img/logo.png"))
        self.label_icon_title = ttk.Label(master, bootstyle="default", image=self.icon_title) 
        self.label_icon_title.place(relx=0.27, rely=0.15)

        # Label Sign up
        self.label_signup = ttk.Label(master, bootstyle="default", text="Home", font=("Helvetica", 25))
        self.label_signup.place(relx=0.54, rely=0.2, anchor=CENTER)
        # Label Sign up
        self.label_advertise = ttk.Label(master, bootstyle="default", text="Create account for free", font=("Helvetica", 10))
        self.label_advertise.place(relx=0.5, rely=0.26, anchor=CENTER)

        # Entry Name
        self.nameFrame = ttk.Labelframe(master, bootstyle="info", text="Name")
        self.nameFrame.place(relx=0.5, rely=0.35, anchor=CENTER)
        self.username = ttk.Entry(self.nameFrame, bootstyle="dark", width=35)
        self.username.pack()
        self.username.insert(0, "username")

        # Entry Email
        self.emailFrame = ttk.Labelframe(master, bootstyle="info", text="Email")
        self.emailFrame.place(relx=0.5, rely=0.45, anchor=CENTER)
        self.email = ttk.Entry(self.emailFrame, bootstyle="dark", width=35)
        self.email.pack()
        self.email.insert(0, "username@gmail.com")
  
        # Entry Password
        self.passwordFrame = ttk.Labelframe(master, bootstyle="info", text="Password")
        self.passwordFrame.place(relx=0.5, rely=0.55, anchor=CENTER)
        self.password = ttk.Entry(self.passwordFrame, bootstyle="dark", width=35)
        self.password.pack()
        self.password.config(show="*")  # Hide password
        # Button hide password with showPassword command
        self.iconHideEye = ImageTk.PhotoImage(Image.open("img/hide.png"))
        self.button_hideEye = ttk.Button(self.passwordFrame, bootstyle="dark-outiline", image=self.iconHideEye, command=self.showPassword) 
        self.button_hideEye.place(relx=1, rely=0.5, anchor=E)

        # Button Generate Password
        self.icon_generate = ImageTk.PhotoImage(Image.open("img/generate.png"))
        self.button_generate = ttk.Button(master, bootstyle="secondary-outline", image=self.icon_generate, command=self.generatePassword)  # Generate password
        self.button_generate.place(relx=0.96, rely=0.565, anchor=E)

        # Button Create Account
        self.button_create = ttk.Button(master, bootstyle="default", text="Create Account", width=25)
        self.button_create.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Label for signup with social midia
        self.label_social = ttk.Label(master, bootstyle="default", text="or sign up with", font=("Helvetica", 9))
        self.label_social.place(relx=0.5, rely=0.83, anchor=CENTER)
        
        # Social midia
        # Facebook icon
        self.fb_icon = ImageTk.PhotoImage(Image.open("img/facebook.png"))
        self.label_fb = ttk.Label(master, bootstyle="default", image=self.fb_icon)
        self.label_fb.place(relx=0.43, rely=0.9, anchor=CENTER)
        # Google icon
        self.google_icon = ImageTk.PhotoImage(Image.open("img/google.png"))
        self.label_google = ttk.Label(master, bootstyle="default", image=self.google_icon)
        self.label_google.place(relx=0.57, rely=0.9, anchor=CENTER)


    def showPassword(self):
        def hidePassword():
            self.password.config(show="*")  # Hide password
            self.button_showEye.destroy()  # Destroy the button show password

        # Button show password with hidePassword command
        self.iconShowEye = ImageTk.PhotoImage(Image.open("img/show.png"))
        self.button_showEye = ttk.Button(self.passwordFrame, bootstyle="dark-outiline", image=self.iconShowEye, command=hidePassword)  
        self.button_showEye.place(relx=1, rely=0.5, anchor=E)

        self.password.config(show="")  # Show password

    
    def generatePassword(self):
        # Get all characters
        letters = string.ascii_letters  
        digits = string.digits
        punctuation = string.punctuation
        new_password = ""

        # Concatenate all characters
        characters = letters + digits + punctuation

        for i in range(15):
            new_password += choice(characters)  # choose each character

        self.password.delete(0, '')  # Delete the text field
        self.password.insert(0, new_password)  # Insert the new password


if __name__ == "__main__":
    app = ttk.Window(
        title="Sign up",
        themename="superhero",
        size=(340, 550),
        resizable=(False, False),
        iconphoto="img/logo.png"
    )
    Window(app)
    app.mainloop()
