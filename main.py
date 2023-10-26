from menu import MenuBar
from style import FG_COLOR
from text_field import TextField
from toolbar import Toolbar


from tkinter import font

import customtkinter as ctk

import os
from PIL import ImageTk



#? For changing title bar color // only works for windows
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

#test git repo

class App(ctk.CTk):
    
    #TITLE_BAR_COLOR = 0x00261918
    
    ICON_PATH = os.path.join("Assets", "quill.png")
    def __init__(self):
        super().__init__()
        self.geometry("1920x1080")
        self.title('')
        #self.resizable(False, False)
        self.configure(fg_color=FG_COLOR)
        
        self.TITLE_BAR_COLOR = 0x00282d2e
        
        #45433b
        #2e2d28
        self.font_families = font.families()
    
        #  Widgets
        
        self.text_field = TextField(self)
        
        self.tool_bar = Toolbar(self, self.font_families,self.text_field )
        
        self.menu_bar = MenuBar(self, self.text_field)
        
        
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
        self.bind_all('<Control-n>', self.text_field.new_file)
        #? Works need to be done for every shortcut
        


    def create_icon(self):
        self.iconpath = ImageTk.PhotoImage(file=self.ICON_PATH)
        self.iconphoto(False, self.iconpath)
    
    def change_titlebar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            
            windll.dwmapi.DwmSetWindowAttribute(HWND, 35, byref(c_int(self.TITLE_BAR_COLOR)), sizeof(c_int))
        except:
            pass
    
    def exit_app(self, event):
        self.destroy()
    
    
 
app = App()

app.mainloop()