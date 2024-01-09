import tkinter as tk 
from tkinter import ttk, messagebox
import customtkinter
import requests
from main import HomePage 

class login:
    def __init__(self,login_frame,registration_frame,home_frame,screen1_frame):
        self.login_frame=login_frame
        self.registration_frame=registration_frame
        self.home_frame=home_frame
        self.screen1_frame=screen1_frame
        self.main_obj=HomePage()
        # Custom Fonts
        title_font = ("Helvetica", 18, "bold")
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")
        # Variables for user input
        self.username_var = tk.StringVar()
        self.password_var = tk.StringVar()


        # Labels
        label_login = ttk.Label(self.login_frame, text="Login", font=("Helvetica", 25, "bold"))
        label_username = ttk.Label(self.login_frame, text="Username:", font=label_font)
        label_password = ttk.Label(self.login_frame, text="Password:", font=label_font)

        # Entry widgets
        entry_username = ttk.Entry(self.login_frame, textvariable=self.username_var, font=entry_font)
        entry_password = ttk.Entry(self.login_frame, textvariable=self.password_var, show="*", font=entry_font)

        # Buttons
        btn_login = ttk.Button(self.login_frame, text="Login",style="Green.TButton",command=self.perform_login)


        # Configure custom styles
        style = ttk.Style()
        style.configure("Green.TButton", foreground="black", background="yellow")


        # Layout using grid
        label_username.grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        label_password.grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        entry_username.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)
        entry_password.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)
        btn_login.grid(row=4, column=0, columnspan=2, pady=10)
        label_login.grid(row=0, column=1, columnspan=2, pady=10)
    def perform_login(self):
        check_counter=0
        if self.username_var.get() == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if self.password_var.get()== "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            try:
                response=requests.post('https://mokshahanshita.pythonanywhere.com/login',{'username':self.username_var.get(),"password":self.password_var.get()})
                print(response)
                messagebox.showinfo("",response.text)
                ausername=self.username_var.get()
                apwd=self.password_var.get()
                self.show_screen1_frame()
                self.main_obj.login_succesfull()


            except Exception as e :
                messagebox.showerror(e)
        else:
            messagebox.showerror('', warn)
    def show_screen1_frame(self):
            # Show login frame and hide registration frame
            self.registration_frame.grid_forget()
            self.home_frame.grid_forget()
            self.login_frame.grid_forget()
            self.screen1_frame.place(x=350,y=200,anchor="center")

    