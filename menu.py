
from style import *


import customtkinter as ctk
from CTkMenuBar import *


class MenuBar(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        
        self.parent = parent
        menu = CTkTitleMenu(parent,  padx=10, y_offset=4)
        
        file_button = menu.add_cascade('File')
        file_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)
      
       
        edit_button = menu.add_cascade("Edit")
        edit_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)
        
        #? Placeholder settings_button = menu.add_cascade("Settings")
        #? Placeholder settings_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)
        
        #? Placeholder about_button = menu.add_cascade("About")
        #? Placeholder about_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)

        

        


        file_dropdown = CustomDropdownMenu(widget=file_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        file_dropdown.add_option(option=NEW_FILE)
        
        
            
        
           
        
        tabWidth = 4
        
        
        #? works but only when you are currently focused on set wigdet         
        #menu.bind('<Control-n>', print_open)
        #menu.bind('<Control-s>', print_save)
        
        file_dropdown.add_option(option=OPEN_FILE, command=lambda: print("Open"))
        file_dropdown.add_option(option=SAVE_FILE, command= lambda: print("Saved"))
        
        file_sub_menu = file_dropdown.add_submenu(EXPORT_AS)
        file_sub_menu.add_option(option=".TXT", command= lambda: print("Hello motherfucker"))
        file_sub_menu.add_option(option=".PDF")
        file_sub_menu.configure(border_width=0, fg_color=MENU_COLOR, corner_radius=5, )
        file_sub_menu.padx=7
        file_sub_menu.pady=7
        
        file_dropdown.add_separator()
        
        def exit_app():
            self.parent.destroy()
    
        file_dropdown.add_option(option=EXIT, command=exit_app)
        
       

        
        edit_dropdown = CustomDropdownMenu(widget=edit_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        edit_dropdown.add_option(option=CUT)
        edit_dropdown.add_option(option=COPY)
        edit_dropdown.add_option(option=PASTE)
        edit_dropdown.add_option(option=FIND)
       
        
        # ? placeholder dropdown3 = CustomDropdownMenu(widget=settings_button)
        # ? placeholder dropdown3.add_option(option="Preferences")
        # ? placeholder dropdown3.add_option(option="Update")

        # ? placeholder dropdown4 = CustomDropdownMenu(widget=about_button)
        # ? placeholder dropdown4.add_option(option="Hello World")#? Placeholder 