from style import *


import customtkinter as ctk


from PIL import Image
from CTkScrollableDropdown import *
from text_field import *
from CTkListbox import *

from CTkColorPicker import *


class Toolbar(ctk.CTkFrame):
    
   
    def __init__(self, parent, fonts, text_field):
        super().__init__(master=parent)
        
        self.italic_image = ctk.CTkImage(dark_image=Image.open("Assets/italic.png"), size=(13,13))
        self.align_left_image = ctk.CTkImage(dark_image=Image.open("Assets/align_left.png"), size=(16,16))
        self.align_center_image = ctk.CTkImage(dark_image=Image.open("Assets/align_center.png"), size=(16,16))
        self.align_right_image = ctk.CTkImage(dark_image=Image.open("Assets/align_right.png"), size=(16,16))
        self.text_spacing_image = ctk.CTkImage(dark_image=Image.open("Assets/spacing.png"), size=(16,16))
        self.grid(row=0, column=1, sticky='nsew')
        self.configure(fg_color=FG_COLOR)
        self.spacing_values = [0.0, 1.0,2.0,3.0,4.0,5.0]
    
        self.fonts = fonts
        self.fonts = [font for font in self.fonts if not font.startswith('@')]
        self.fonts = sorted(self.fonts)
        
        self.selection_start = None
        self.selection_end = None
        self.isBold = False
        self.isItalic = False
        self.text = text_field
        
        self.default_textfield_font_size = 16
        self.font = 'Arial'
        
        self.font_size_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.font_size_frame.pack(side='left', padx=10, anchor='center')
        
        self.font_button = ctk.CTkButton(self.font_size_frame, text='Arial', width=100, text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16 ), anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR)
        self.font_button.pack(side='left', padx=4, pady=4)
        
        self.font_size_button = ctk.CTkButton(self.font_size_frame, text=str(self.default_textfield_font_size),text_color=TEXT_COLOR ,width=30, fg_color=BUTTON_COLOR, font=('Segoe UI Variable', 16 ), corner_radius=5, hover_color=BUTTON_HOVER_COLOR)
        self.font_size_button.pack(side='left', pady=4, padx= 4)
        
        
        CTkScrollableDropdown(self.font_button, values=self.fonts, height=270,  button_height=30, width=300,
                      scrollbar=True, resize=False, command=self.change_font)
        
        
        CTkScrollableDropdown(self.font_size_button, values=tuple(range(8,81)), height=270,  button_height=30, width=300,
                      scrollbar=True, resize=False, command=self.change_font_size)
        
        self.bold_italic_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.bold_italic_frame.pack(side='left', padx=10, anchor='center')
        
        self.bold_button =ctk.CTkButton(self.bold_italic_frame, text='B', text_color=TEXT_COLOR,width=25, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16, 'bold' ), anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR, command=self.bold_text)
        self.bold_button.pack(side='left', pady=4, padx=4)
        
        self.italic_button =ctk.CTkButton(self.bold_italic_frame, text='',width=25, fg_color=BUTTON_COLOR, anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.italic_image, command=self.italic_text)
        self.italic_button.pack(side='left', pady=4, padx=4)
        
        self.underline_button =ctk.CTkButton(self.bold_italic_frame, text='U',width=25,text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16, 'underline' ), anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR)
        self.underline_button.pack(side='left', pady=4, padx=4)
        
        
        
        self.align_text_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.align_text_frame.pack(side='left', padx=10, anchor='center')
        
        self.align_left =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_left_image)
        self.align_left.pack(side='left', pady=4, padx=4)
        
        self.align_center =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_center_image)
        self.align_center.pack(side='left', pady=4, padx=4)
        
        self.align_right =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_right_image)
        self.align_right.pack(side='left', pady=4, padx=4)
        
        
        self.spacing_color_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.spacing_color_frame.pack(side='left', padx=10, anchor='center')
        
        self.spacing_button =ctk.CTkButton(self.spacing_color_frame, text='0.0',text_color=TEXT_COLOR,width=25, fg_color=BUTTON_COLOR, anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.text_spacing_image)
        self.spacing_button.pack(side='left', pady=4, padx=4)
        
        
        CTkScrollableDropdown(self.spacing_button, values=self.spacing_values, width=150,
                      scrollbar=True, command=self.change_spacing)
        
       
       
        self.color_picker_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.color_picker_frame.pack(side='left', padx=10, anchor='center')
        self.color_button = ctk.CTkButton(master=self.color_picker_frame, text="CHOOSE COLOR", text_color="black", command=self.ask_color)
        self.color_button.pack(side='left', pady=4, padx=4)
       

    def ask_color(self):
        pick_color = AskColor() # open the color picker
        color = pick_color.get() # get the color string
        self.text.configure(fg=color)
    def change_spacing(self, selected_spacing):
        
        self.text.configure(spacing1=selected_spacing)
        self.spacing_button.configure(text=selected_spacing)
        
    def bold_text(self):
        try:
            self.selection_start = self.text.index('sel.first')
            self.selection_end = self.text.index('sel.last')
        except:
            return

        if self.selection_start == self.selection_end:
            # No text is selected, just exit
            return

        current_tags = self.text.tag_names(self.selection_start)

        # Toggle bold state
        if self.isBold:
            self.text.tag_remove('bold', self.selection_start, self.selection_end)
        else:
            self.text.tag_add('bold', self.selection_start, self.selection_end)
            self.text.tag_configure('bold', font=(self.font, self.default_textfield_font_size, 'bold'))

        # Check for existing italic tag and add it if present
        if 'italic' in current_tags:
            self.text.tag_add('bolditalic', self.selection_start, self.selection_end)
            self.text.tag_configure('bolditalic', font=(self.font, self.default_textfield_font_size, 'bold italic'))

        # Update the bold state
        self.isBold = not self.isBold

        # Deselect the text
        self.text.tag_remove("sel", "1.0", "end")

    def italic_text(self):
       
       
        try:
            self.selection_start = self.text.index('sel.first')
            self.selection_end = self.text.index('sel.last')
            self.text.tag_add('italic', self.selection_start, self.selection_end)
        except:
            self.selection_start = None
            self.selection_end = None

       
       
        if self.isItalic == False and (self.selection_start and self.selection_end) is None:
                 self.text.configure(font=(self.font, self.default_textfield_font_size, 'italic'))
                 self.isItalic = True
                 
        elif self.isItalic == True and (self.selection_start and self.selection_end) is None:
                self.text.configure(font=(self.font, self.default_textfield_font_size))
                self.isItalic = False
                
        elif self.isItalic == False and (self.selection_start and self.selection_end) is not None:  
                self.text.tag_config('italic', font=(self.font, self.default_textfield_font_size, 'italic'))
                self.isItalic = True
                
                
        elif self.isItalic == True and (self.selection_start and self.selection_end) is not None:  
                self.text.tag_config('italic', font=(self.font, self.default_textfield_font_size))
                self.isItalic = False
                self.text.tag_remove('italic', self.selection_start, self.selection_end)
            
        
            
           
        
    
    def change_font(self, selected_font):
        
        
        self.font = selected_font
        
        
        display_font = selected_font if len(selected_font) <= 10 else selected_font[:10] + "..."
        self.font_button.configure(text=display_font)
        
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
        
        self.font_size_button.configure(text=self.default_textfield_font_size)
      

 
       
     