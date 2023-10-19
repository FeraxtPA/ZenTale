from style import *


import customtkinter as ctk

from tkinter import font
from CTkScrollableDropdown import *
from text_field import *



class Toolbar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        self.grid(row=0, column=0,columnspan=3, sticky='nsew')
        self.configure(fg_color=FG_COLOR)
        
        self.font_families = font.families()
        
        self.text = TextField(parent)
        
        
        
        
        self.button = ctk.CTkButton(self, text='Font', width=100, fg_color=FONTBOX_COLOR, font=('Segoe UI Variable', 16 ), command=self.change_color)
        self.button.pack(side='left', padx=10)
        CTkScrollableDropdown(self.button, values=self.font_families, height=270, resize=True, button_height=30, width=300,
                      scrollbar=True, autocomplete=True)
        
        
    
    def change_color(self):
        self.text.configure(text_color='black')

        
     