
from style import *

import customtkinter as ctk
from CTkMenuBar import *

import os
from PIL import ImageTk

#? For changing title bar color // only works for windows
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass



class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title('')
        self.resizable(False, False)
        self.configure(fg_color=FG_COLOR)
        #  Widgets
        self.menu_bar = MenuBar(self)
        
        self.label = ctk.CTkLabel(self, text=':)',  font=('Segoe UI Variable', 300 ), anchor='center').pack(side='top', expand=True, fill='both')
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
        
        settings_button = menu.add_cascade("Settings")
        settings_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)
        
        about_button = menu.add_cascade("About")
        about_button.configure(  fg_color='transparent', hover_color=HOVER_COLOR, font=('Segoe UI Variable', 16 ),anchor='center', text_color=TEXT_COLOR)

        dropdown1 = CustomDropdownMenu(widget=file_button, border_width=0, font=('Segoe UI Variable', 16 ), text_color=TEXT_COLOR, bg_color=MENU_COLOR, separator_color=SEPARATOR_COLOR, corner_radius=5, hover_color=HOVER_MENU_COLOR)
        
        
            
        dropdown1.add_option(option=NEW_FILE, command=lambda: print("New"))
        
        def print_open(event):
            print('HEllo')
            
        def print_save(event):
            print('Saved')
           
        
        #? works but only when you are currently focused on set wigdet         
        #menu.bind('<Control-n>', print_open)
        menu.bind('<Control-s>', print_save)
        
        dropdown1.add_option(option=OPEN_FILE, command=lambda: print("Open"))
        dropdown1.add_option(option=SAVE_FILE, command= lambda: print("Saved"))

       

        sub_menu = dropdown1.add_submenu(EXPORT_AS)
        
        sub_menu.add_option(option=".TXT", command= lambda: print("Hello motherfucker"))
        sub_menu.add_option(option=".PDF")

        sub_menu.configure(border_width=0, fg_color=MENU_COLOR, corner_radius=5, )
        sub_menu.padx=7
        sub_menu.pady=7
        
        dropdown1.add_separator()
        
        def exit_app():
            self.parent.destroy()
    
        dropdown1.add_option(option=EXIT, command=exit_app)
        
        dropdown2 = CustomDropdownMenu(widget=edit_button)
        dropdown2.add_option(option="Cut")
        dropdown2.add_option(option="Copy")
        dropdown2.add_option(option="Paste")

        dropdown3 = CustomDropdownMenu(widget=settings_button)
        dropdown3.add_option(option="Preferences")
        dropdown3.add_option(option="Update")

        dropdown4 = CustomDropdownMenu(widget=about_button)
        dropdown4.add_option(option="Hello World")
        
        
 
app = App()

app.mainloop()