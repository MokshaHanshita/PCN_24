import tkinter as tk 
from tkinter import ttk, messagebox
from customtkinter import *
import requests
class Page1:
    def __init__(self,screen1):
        self.screen1 = screen1
        label_welcome = ttk.Label(self.screen1, text="hi")
        label_welcome.grid(column=4,row=2)