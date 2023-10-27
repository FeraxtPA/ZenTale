from style import *

import os
import customtkinter as ctk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
import tkinter as tk
from tkinter import filedialog
from state_bar import*

class TextField(tk.Text):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        self.grid(row=1, column=1,sticky='nsew')
        
        self.state_bar = None
        
        self.url = ''
        self.parent = parent
        self.scrollbar_frame = ctk.CTkFrame(parent,fg_color='white', width=10)
        self.scrollbar_frame.grid(row=1, column=2, sticky='nsw')
        
        
        self.scrollbar = ctk.CTkScrollbar(self.scrollbar_frame,command=self.yview, button_color=BUTTON_COLOR,  button_hover_color=BUTTON_HOVER_COLOR, fg_color=TEXT_FIELD_COLOR)
        self.scrollbar.pack(fill='both', expand=True)
        
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
                       insertwidth=4,
                       inactiveselectbackground='#148e9b')
                       
      
        
        
        self.bind('<Control-BackSpace>', lambda event: self.delete_whole_word(event))
        
        
        
    def set_state_bar(self, state_bar):
        self.state_bar = state_bar    
         
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


    def new_file(self, event=None):
        
        msg = CTkMessagebox(title="New File", message="Are you sure you want to create a new file?",
                  option_1="Cancel", option_2="Yes")
        response = msg.get()
        
        if response == 'Yes':
           self.url= ''
           self.delete(0.0, "end")
           self.state_bar.get_words(event)
        else:
            pass
    
    def open_file(self, event=None):
        self.url =filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File','.txt'),
                                                                                            ('Rich Text File', '.rtf'),
                                                                                            ('All Files', '*.*')))
        
        if self.url != '':
            data = open(self.url, 'r')
            self.insert(0.0, data.read())
            text = os.path.basename(self.url)
            self.state_bar.change_title(text)
    
    def save_file_as_txt(self, event=None):
        if self.url == '':
            save_url =filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '.txt'),
                                                                                             ('All Files', '*.*')))
            content = self.get(0.0, 'end')
            save_url.write(content)
            save_url.close()
        else:
            content =self.get(0.0, 'end')
            file=open(self.url,'w')
            file.write(content)
            self.state_bar.show_saved_message()
            self.after(1000, self.state_bar.hide_saved_message)

            
        