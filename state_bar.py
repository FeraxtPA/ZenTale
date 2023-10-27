from style import *
import os

import customtkinter as ctk


class StateBar(ctk.CTkFrame):
    def __init__(self, parent, text_field):
        super().__init__(master=parent)
        
        
        self.text = text_field
        
        self.configure(fg_color='#2e2d28',
                       corner_radius=0,
                       )
        self.grid(row=2, column=0, columnspan=3, sticky='nsew')
        
        self.characters_label = ctk.CTkLabel(self, text='Characters', text_color=TEXT_COLOR, font=('Segoe UI Variable',16 ))
        self.characters_label.pack(side='right', padx=(0,20))
        
        self.words_label = ctk.CTkLabel(self, text='Words', text_color=TEXT_COLOR, font=('Segoe UI Variable',16 ))
        self.words_label.pack(side='right', padx=(0,10))
        
        self.lines_label = ctk.CTkLabel(self, text='Lines', text_color=TEXT_COLOR, font=('Segoe UI Variable',16 ))
        self.lines_label.pack(side='right', padx=(0,10))
        
        self.file_title = ctk.CTkLabel(self, text='Untitled', text_color=TEXT_COLOR, font=('Segoe UI Variable',16 ))
        self.file_title.place(relx=0.5,rely=0.5, anchor='center')
        self.saved_message = ctk.CTkLabel(self, text="File saved", text_color='#94b61c', font=('Segoe UI Variable',16 ))
        self.saved_message.pack(side="left", padx=20)
        self.saved_message.pack_forget()
        self.text.bind('<KeyRelease>', self.get_words)
    
    def get_words(self,event):
        words = self.text.get( '1.0', 'end-1c' )
        words_length = len(words.split())
        lines = int(self.text.index('end-1c').split('.')[0])
        
        self.characters_label.configure(text=f"Characters {len(words)}")
        self.lines_label.configure(text=f"Lines {lines}")
        self.words_label.configure(text=f"Words {words_length}")
        
    def change_title(self, name):
        self.file_title.configure(text=name)
        self.get_words(name)
    
    def show_saved_message(self):
        self.saved_message.pack(side="left", padx=20)

    def hide_saved_message(self):
        self.saved_message.pack_forget()