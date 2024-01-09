import tkinter as tk 
from tkinter import ttk, messagebox
from customtkinter import *
import requests

class registration:
    def __init__(self,registration_frame):
        self.registration_frame=registration_frame
        title_font = ("Helvetica", 18, "bold")
        label_font = ("Helvetica", 12)
        entry_font = ("Helvetica", 12)
        button_font = ("Helvetica", 12, "bold")

        self.name_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.phonenum_var = tk.StringVar()
        self.pwd_var = tk.StringVar()
        self.pwd_again_var = tk.StringVar()
        self.last_name_var = tk.StringVar()

        # Labels
        label_registration = ttk.Label(self.registration_frame, text="Registration Form", font=("Helvetica", 14, "bold"))

        # Create a CTkentry
        self.name_entry = CTkEntry(self.registration_frame,textvariable=self.name_var)

        self.mail_entry = CTkEntry(self.registration_frame,textvariable=self.email_var)

        self.phone_num_entry = CTkEntry(self.registration_frame,textvariable=self.phonenum_var)

        self.pwd_entry  =  CTkEntry(self.registration_frame,textvariable=self.pwd_var)
        self.pwd_again_entry  =  CTkEntry(self.registration_frame,textvariable=self.pwd_again_var)

        self.last_name = CTkEntry(self.registration_frame,textvariable=self.last_name_var)
    

        # Create a new CTklabel widget
        name_label = CTkLabel(self.registration_frame,text="Enter your Name ")

        mail_label = CTkLabel(self.registration_frame,text="Enter your Email address ")

        phone_num_label = CTkLabel(self.registration_frame,text="Enter your Phone Number ")

        pwd  = CTkLabel(self.registration_frame,text="Enter your password ")

        pwd_again = CTkLabel(self.registration_frame,text=" Confirm password")
        Last_name  = CTkLabel(self.registration_frame,text="Enter you last name ")
        # create register button
        button=CTkButton(self.registration_frame,text="Register",command=self.perform_registration)

        # Configure custom styles
        style = ttk.Style()
        style.configure("Red.TButton", foreground="white", background="#e74c3c")

        # Layout for registration frame
        label_registration.grid(row=0, column=0, columnspan=2, pady=10)
        # Add the CTkEntry widget to the window
        self.name_entry.grid(row=4,column=0)
        self.mail_entry.grid(row=8,column=0)
        self.phone_num_entry.grid(row=8,column=5)
        self.pwd_entry.grid(row=12,column=0)
        self.pwd_again_entry.grid(row=12,column=5)
        self.last_name.grid(row=4,column=5)
        

        # Add the label to the window
        name_label.grid(row=2,column=0,pady=10)
        mail_label.grid(row=6,column=0,pady=10)
        phone_num_label.grid(row=6,column=5,pady=10)
        pwd.grid(row=10,column=0,pady=10)
        pwd_again.grid(row=10,column=5,pady=10)
        Last_name.grid(row=2,column=5,pady=10)
        #add the button
        button.grid(row=22,column=2,pady=10)
    def perform_registration(self):
        check_counter=0
        warn = ""
        if self.name_var.get() == "":
            warn = "Name can't be empty"
        else:
            print(self.name_var.get())
            check_counter += 1
            
        if self.email_var.get() == "":
            warn = "Email can't be empty"
        else:
            print(self.email_var.get())
            check_counter += 1

        if self.phonenum_var.get() == "":
            warn = "Contact can't be empty"
        else:
            print(self.phonenum_var.get())
            check_counter += 1
        

        if self.pwd_var.get() == "":
            warn = "Password can't be empty"
        else:
            print(self.pwd_var.get())
            check_counter += 1

        if self.pwd_again_var.get() == "":
            warn = "Re-enter password can't be empty"
        else:
            print(self.pwd_again_var.get())
            check_counter += 1

        if self.pwd_var.get() != self.pwd_again_var.get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1
        print(check_counter)
        if check_counter == 6:       
            try:
                    response=requests.post('https://mokshahanshita.pythonanywhere.com/register',{'username':self.email_var.get(),"password":self.pwd_var.get()})
                    print(response)
                    messagebox.showinfo('confirmation', 'Record Saved')
                    self.name_entry.delete(0,END)
                    self.mail_entry.delete(0,END)
                    self.phone_num_entry.delete(0,END)
                    self.pwd_entry.delete(0,END)
                    self.pwd_again_entry.delete(0,END)


            except Exception as ep:
                messagebox.showerror('', ep) 
                print(ep)
        else:
            messagebox.showerror('Error', warn)
