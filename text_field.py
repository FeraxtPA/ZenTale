from style import *


import customtkinter as ctk




        
class TextField(ctk.CTkTextbox):
    def __init__(self, parent):
        super().__init__(master=parent)
        
        self.grid(row=1, column=1,rowspan=2, sticky='nsew', pady=5, padx=5)
        
        self.configure(fg_color=TEXT_FIELD_COLOR,
                       text_color= TEXT_COLOR,
                       font=('Segoe UI Variable', 16 ),
                       scrollbar_button_color=SCROLLBAR_COLOR,
                       scrollbar_button_hover_color=HOVER_SCROLLBAR_COLOR)
        
        
        
        self.bind('<Control-BackSpace>', lambda event: self.delete_whole_word(event))

         
    def delete_whole_word(self, event):
        text_widget = event.widget
        cursor_pos = text_widget.index(ctk.INSERT)
        line_start = f"{cursor_pos.split('.')[0]}.0"  # Get the start of the current line
        text_before_cursor = text_widget.get(line_start, cursor_pos)  # Get text from line start to cursor position

        # Use a regular expression to find the word preceding the cursor
        import re
        word_match = re.search(r'\S*\s*$', text_before_cursor)

        if word_match:
            start, end = word_match.span()
            text_widget.delete(line_start + "+%dc" % start, cursor_pos)

        return "break"  # Prevent the default behavior


