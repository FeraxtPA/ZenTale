
from style import *

import customtkinter as ctk
from CTkMenuBar import *

import os
from PIL import ImageTk
from CTkListbox import *


#? For changing title bar color // only works for windows
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

#test git repo

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title('')
        self.resizable(False, False)
        self.configure(fg_color=FG_COLOR)
        #  Widgets
        self.menu_bar = MenuBar(self)
        
        self.text = ctk.CTkTextbox(self,font=('Segoe UI Variable', 16 ), width=800, height=1100).pack(side='top', fill='y', pady=20, padx=20)
        # * Title bar and Icon
        self.change_titlebar_color()
        self.create_icon()
        
        #self.textbox = ctk.CTkTextbox(self, width=500, height=700).pack()
        
        self.bind_all('<Control-q>', self.exit_app)
        #? Works need to be done for every shortcut
    def ptest(self, event):
            print('Window bind')
    def create_icon(self):
        self.iconpath = ImageTk.PhotoImage(file=os.path.join("Assets","quill.png"))
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)    
    
    def change_titlebar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            title_bar_color = 0x00261918
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))
        except:
            pass
    
    def exit_app(self, event):
        self.destroy()
    
    
            
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

        def print_save():
            print('Hey')

        
        file_dropdown = CustomDropdownMenu(widget=file_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        file_dropdown.add_option(option=NEW_FILE, command=print_save)
        
        def print_open(event):
            print('HEllo')
            
        
           
        
        #? works but only when you are currently focused on set wigdet         
        #menu.bind('<Control-n>', print_open)
        menu.bind('<Control-s>', print_save)
        
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
        
        
 
app = App()

app.mainloop()