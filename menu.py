
from style import *


import customtkinter as ctk
from CTkMenuBar import *
from text_field import *

class MenuBar(CTkTitleMenu):
    
    
    def __init__(self, parent, text_field):
        super().__init__(master=parent)
        
        self.text = text_field
        
        self.file_button = self.add_cascade('File')
        self.file_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color='#e8e0c2')
      
       
        self.edit_button = self.add_cascade("Edit")
        self.edit_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color='#e8e0c2')
        
        #? Placeholder settings_button = menu.add_cascade("Settings")
        #? Placeholder settings_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)
        
        #? Placeholder about_button = menu.add_cascade("About")
        #? Placeholder about_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)

        

       
           

        
        self.file_dropdown = CustomDropdownMenu(widget=self.file_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        self.file_dropdown.add_option(option=NEW_FILE, command=lambda: self.text.delete(0.0, "end"))
        
     
            
        
       
        
        
        #? works but only when you are currently focused on set wigdet         
        #menu.bind('<Control-n>', print_open)
        #menu.bind('<Control-s>', print_save)
        
        self.file_dropdown.add_option(option=OPEN_FILE, command=lambda: print("Open"))
        self.file_dropdown.add_option(option=SAVE_FILE, command= lambda: print("Saved"))
        
        self.file_sub_menu = self.file_dropdown.add_submenu(EXPORT_AS)
        self.file_sub_menu.add_option(option=".TXT", command= lambda: print("Hello motherfucker"))
        self.file_sub_menu.add_option(option=".PDF")
        self.file_sub_menu.configure(border_width=0, fg_color=MENU_COLOR, corner_radius=5, )
        self.file_sub_menu.padx=7
        self.file_sub_menu.pady=7
        
        self.file_dropdown.add_separator()
        
        def exit_app():
            parent.destroy()
    
        self.file_dropdown.add_option(option=EXIT, command=exit_app)
        
       

        
        self.edit_dropdown = CustomDropdownMenu(widget=self.edit_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        self.edit_dropdown.add_option(option=CUT)
        self.edit_dropdown.add_option(option=COPY)
        self.edit_dropdown.add_option(option=PASTE)
        self.edit_dropdown.add_option(option=FIND)

    
    
    