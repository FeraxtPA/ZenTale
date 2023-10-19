from menu import *
from style import *
from text_field import *
from toolbar import *


import customtkinter as ctk
from CTkMenuBar import *

import os
from PIL import ImageTk
import tkinter as tk


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
        #self.resizable(False, False)
        self.configure(fg_color=FG_COLOR)
        #  Widgets
        self.menu_bar = MenuBar(self)
        self.text_field = TextField(self)
        self.tool_bar = Toolbar(self)
        
        self.rowconfigure(0, weight=1, uniform='a')
        self.rowconfigure(1, weight=20, uniform='a')
        self.rowconfigure(2, weight=1, uniform='a')
        
        self.columnconfigure(0, weight=3, uniform='a')
        self.columnconfigure(1, weight=4, uniform='a')
        self.columnconfigure(2, weight=3, uniform='a')
        
        # * Title bar and Icon
        self.change_titlebar_color()
        self.create_icon()
        
        
        
        self.bind_all('<Control-q>', self.exit_app)
        #? Works need to be done for every shortcut
        


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
    
    
 
app = App()

app.mainloop()