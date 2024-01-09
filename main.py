import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter
from register import registration
from login import login
from screen1 import Page1
from PIL import ImageTk
from PIL import Image, ImageTk

class HomePage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sample Title")
        self.root.geometry("700x600")
        self.root.resizable(False,False)

        #creating menu bar
        self.show_menu()



        # Create frames
        self.home_frame = ttk.Frame(self.root)
        self.login_frame = ttk.Frame(self.root)
        self.registration_frame = ttk.Frame(self.root)
        self.screen1_frame = ttk.Frame(self.root)
        login_obj=login(self.login_frame,self.registration_frame,self.home_frame,self.screen1_frame,self.login_succesfull)
        register_obj=registration(self.registration_frame)
        screen1_obj=Page1(self.screen1_frame)


        #set up home frame
        self.create_home_frame()

    
    def create_home_frame(self):
        text=tk.Label(self.home_frame,text="sample Text")
        text.grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.show_home_frame()
    


    def create_login_frame(self):
        self.show_login_frame()

    def create_registration_frame(self):
        self.show_registration_frame()

    def show_home_frame(self):
        # Show home frame and hide login frame
        self.login_frame.place_forget()
        self.registration_frame.grid_forget()
        self.home_frame.grid(row=0, column=0, padx=10, pady=10)
    
    
    def show_login_frame(self):
        # Show login frame and hide registration frame
        self.registration_frame.grid_forget()
        self.home_frame.grid_forget()
        self.login_frame.place(x=350,y=200,anchor="center")


    def show_registration_frame(self):
        # Show registration frame and hide login frame
        self.login_frame.place_forget()
        self.home_frame.grid_forget()
        self.registration_frame.grid(row=0, column=0, padx=10, pady=10)
    
    def show_menu(self,status):
        if status==False:
            self.menubar = tk.Menu(self.root)
            self.file_menu = tk.Menu(self.menubar)
            self.menubar.add_cascade(label="Home",command=self.create_home_frame)
            self.menubar.add_cascade(label="Registration",command=self.create_registration_frame)
            self.menubar.add_cascade(label="Login",command=self.create_login_frame)
            self.root.config(menu=self.menubar)
        else:
            self.menubar = tk.Menu(self.root)
            self.file_menu = tk.Menu(self.menubar)
            self.menubar.add_cascade(label="Home",command=self.create_home_frame)
            self.root.config(menu=self.menubar)
    def login_succesfull(self):
        self.show_menu(True)

        


    


if __name__ == "__main__":
    root = tk.Tk()
    app = HomePage(root)
    root.mainloop()