from style import *


import customtkinter as ctk
from tkinter import ttk

import tkinter as tk

        
class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        self.grid(row=1, column=1,rowspan=2, sticky='nsew', pady=5, padx=5)
        
        
        
        self.scrollbar = ctk.CTkScrollbar(self, command=self.yview, button_color=BUTTON_COLOR,  button_hover_color=BUTTON_HOVER_COLOR, fg_color=TEXT_FIELD_COLOR)
        self.scrollbar.pack(side='right', fill='y')
        
        
        self.configure(bg=TEXT_FIELD_COLOR,
                       fg=TEXT_FIELD_TEXT_COLOR,
                       bd=0,
                       font=('Segoe UI Variable', 16 ),
                       insertbackground='#148e9b',
                       relief='flat',
                       selectbackground='#148e9b',
                       yscrollcommand=self.scrollbar.set,
                       undo=True,
                       maxundo=1,
                       inactiveselectbackground='#148e9b')
                       
      
        
        
        self.bind('<Control-BackSpace>', lambda event: self.delete_whole_word(event))

         
    def delete_whole_word(self, event):
        text_widget = event.widget
        cursor_pos = text_widget.index(tk.INSERT)
        line_start = f"{cursor_pos.split('.')[0]}.0"  # Get the start of the current line
        text_before_cursor = text_widget.get(line_start, cursor_pos)  # Get text from line start to cursor position

        # Use a regular expression to find the word preceding the cursor
        import re
        word_match = re.search(r'\S*\s*$', text_before_cursor)

        if word_match:
            start, end = word_match.span()
            text_widget.delete(line_start + "+%dc" % start, cursor_pos)

        return "break"  # Prevent the default behavior


