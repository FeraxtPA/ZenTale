from style import *


import customtkinter as ctk


from CTkScrollableDropdown import *
from text_field import *


class Toolbar(ctk.CTkFrame):
    def __init__(self, parent, fonts):
        super().__init__(master=parent)
        
        self.grid(row=0, column=0,columnspan=3, sticky='nsew')
        self.configure(fg_color=FG_COLOR)
        
        self.fonts = fonts
        self.fonts = [font for font in self.fonts if not font.startswith('@')]
        self.fonts = sorted(self.fonts)
        
        self.selection_start = None
        self.selection_end = None
            
        self.text = TextField(parent)
        
        self.default_textfield_font_size = 16
        self.font = 'Arial'
        
        self.font_size_frame = ctk.CTkFrame(self, fg_color='white', width=200, height=100)
        self.font_size_frame.pack(side='left', padx=10)
        
        self.button = ctk.CTkButton(self.font_size_frame, text='Arial', width=100, fg_color=FONTBOX_COLOR, font=('Segoe UI Variable',16 ), anchor='center')
        self.button.pack(side='left', padx=2, expand=False)
        
        
        
       
        
        self.button2 = ctk.CTkButton(self.font_size_frame, text=str(self.default_textfield_font_size), width=30, fg_color=FONTBOX_COLOR, font=('Segoe UI Variable', 16 ))
        self.button2.pack(side='left')
        
        
        CTkScrollableDropdown(self.button, values=self.fonts, height=270,  button_height=30, width=300,
                      scrollbar=True, resize=False, command=self.change_font)
        
        
        CTkScrollableDropdown(self.button2, values=tuple(range(8,81)), height=270,  button_height=30, width=300,
                      scrollbar=True, resize=False, command=self.change_font_size)
        
        
  
    
        
        

  
        
        
    def change_font(self, selected_font):
        
        
        self.font = selected_font
        
        
        if len(selected_font) > 10:
                selected_font = selected_font[:10] + "..."
                self.button.configure(text=selected_font)
        else:
                self.button.configure(text=selected_font)
        try:
            self.selection_start = self.text.index('sel.first')
            self.selection_end = self.text.index('sel.last')
            self.text.tag_add('color', self.selection_start, self.selection_end)
        except:
            pass
        
        
        if (self.selection_start and self.selection_end) is  None:
            
            self.text.configure(font=(self.font, self.default_textfield_font_size))
        
        else:
            self.text.configure(font=(self.font, self.default_textfield_font_size))
        
            self.text.tag_config('color', foreground='red')

    def change_font_size(self, selected_size):
        
        self.default_textfield_font_size = selected_size
        
        self.text.configure(font=(self.font, self.default_textfield_font_size))
        
        self.button2.configure(text=self.default_textfield_font_size)
      

 
       
     