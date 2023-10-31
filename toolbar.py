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
        self.text_color_image = ctk.CTkImage(dark_image=Image.open("Assets/text_color.png"), size=(16,16))
        self.grid(row=0, column=1, sticky='nsew')
        self.configure(fg_color=FG_COLOR)
        self.spacing_values = [0.0, 1.0,2.0,3.0,4.0,5.0]

        self.fonts = fonts
        self.fonts = [font for font in self.fonts if not font.startswith('@')]
        self.fonts = sorted(self.fonts)
        
        self.picker_active = False
        self.selection_start = None
        self.selection_end = None
        self.isBold = False
        self.isItalic = False
        self.text = text_field
      
        
        self.default_textfield_font_size = 16
        self.font = 'Arial'
        
        self.font_style = []
        self.styles =  []
        
        self.color_picker = CTkColorPicker(width=500, command=self.ask_color, orientation='horizontal', corner_radius=5, fg_color="#69625a", button_color=BUTTON_COLOR, button_hover_color=BUTTON_HOVER_COLOR)
        
        self.font_pressed = False
      
        self.font_size_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.font_size_frame.pack(side='left', padx=10, anchor='center')
        
        self.font_button = ctk.CTkButton(self.font_size_frame, text='Arial', width=100, text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16 ), anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR)
        self.font_button.pack(side='left', padx=4, pady=4)
        
        self.font_size_button = ctk.CTkButton(self.font_size_frame, text=str(self.default_textfield_font_size),text_color=TEXT_COLOR ,width=30, fg_color=BUTTON_COLOR, font=('Segoe UI Variable', 16 ), corner_radius=5, hover_color=BUTTON_HOVER_COLOR, )
        self.font_size_button.pack(side='left', pady=4, padx= 4)
        
        
        CTkScrollableDropdown(self.font_button, values=self.fonts, height=290,  button_height=30, width=300,
                      scrollbar=True,  command=self.change_font, frame_corner_radius=8, frame_border_width=0, scrollbar_button_color=BUTTON_COLOR, scrollbar_button_hover_color=BUTTON_HOVER_COLOR,
                      button_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, fg_color='#69625a',text_color=TEXT_COLOR)
        
        
        CTkScrollableDropdown(self.font_size_button, values=tuple(range(8,81)), height=300,  button_height=30, width=300,
                      scrollbar=True, resize=False, command=self.change_font_size,frame_corner_radius=8, frame_border_width=0, scrollbar_button_color=BUTTON_COLOR, scrollbar_button_hover_color=BUTTON_HOVER_COLOR,
                      button_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, fg_color='#69625a',text_color=TEXT_COLOR)
        
        self.bold_italic_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.bold_italic_frame.pack(side='left', padx=10, anchor='center')
        
        self.bold_button =ctk.CTkButton(self.bold_italic_frame, text='B', text_color=TEXT_COLOR,width=25, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16, 'bold' ), anchor='center', corner_radius=5, 
                                        hover_color=BUTTON_HOVER_COLOR,  command= self.bold_text_test)
        self.bold_button.pack(side='left', pady=4, padx=4)
        
        self.italic_button =ctk.CTkButton(self.bold_italic_frame, text='',width=25, fg_color=BUTTON_COLOR, anchor='center', corner_radius=5, 
                                          hover_color=BUTTON_HOVER_COLOR, image=self.italic_image, command= self.italic_text_test)
        self.italic_button.pack(side='left', pady=4, padx=4)
        
        self.underline_button =ctk.CTkButton(self.bold_italic_frame, text='U',width=25,text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, font=('Segoe UI Variable',16, 'underline' ), anchor='center', corner_radius=5, 
                                             hover_color=BUTTON_HOVER_COLOR, command=self.underline_text_test)
        self.underline_button.pack(side='left', pady=4, padx=4)
        
        
        
        self.align_text_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.align_text_frame.pack(side='left', padx=10, anchor='center')
        
        self.align_left =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_left_image, command = lambda: self.align_text('left'))
        self.align_left.pack(side='left', pady=4, padx=4)
        
        self.align_center =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_center_image, command = lambda: self.align_text('center'))
        self.align_center.pack(side='left', pady=4, padx=4)
        
        self.align_right =ctk.CTkButton(self.align_text_frame, text='',width=25, fg_color=BUTTON_COLOR,  corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.align_right_image, command = lambda: self.align_text('right'))
        self.align_right.pack(side='left', pady=4, padx=4)
        
      
        
        
        self.spacing_color_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.spacing_color_frame.pack(side='left', padx=10, anchor='center')
        
        self.spacing_button =ctk.CTkButton(self.spacing_color_frame, text='0.0',text_color=TEXT_COLOR,width=25, fg_color=BUTTON_COLOR, anchor='center', corner_radius=5, hover_color=BUTTON_HOVER_COLOR, image=self.text_spacing_image)
        self.spacing_button.pack(side='left', pady=4, padx=4)
        
       
        
        CTkScrollableDropdown(self.spacing_button, values=self.spacing_values, width=150,
                      scrollbar=True, command=self.change_spacing, frame_corner_radius=8, frame_border_width=0, scrollbar_button_color=BUTTON_COLOR, scrollbar_button_hover_color=BUTTON_HOVER_COLOR,
                      button_color=BUTTON_COLOR, hover_color=BUTTON_HOVER_COLOR, fg_color='#69625a',text_color=TEXT_COLOR)
        
       
        self.color_picker_frame = ctk.CTkFrame(self, fg_color=TEXT_FIELD_COLOR, corner_radius=5)
        self.color_picker_frame.pack(side='left', padx=10, anchor='center')
        self.color_button = ctk.CTkButton(master=self.color_picker_frame, text="", text_color=TEXT_COLOR, fg_color=BUTTON_COLOR, command=self.create_color_frame, hover_color=BUTTON_HOVER_COLOR, width=25, image=self.text_color_image)
        self.color_button.pack(side='left', pady=4, padx=4)
        

   
   
   
        
        
    def align_text(self, align):
        
        try:
            sel_start = self.text.index(tk.SEL_FIRST)
            sel_end = self.text.index(tk.SEL_LAST)
        except:
            sel_start = None
            sel_end = None

        if sel_start and sel_end:
            # Get the text within the selection
            selected_text = self.text.get(sel_start, sel_end)

            # Apply alignment to the selected text
            self.text.tag_configure(f'align_{sel_start}', justify=align)
            self.text.tag_add(f'align_{sel_start}', sel_start, sel_end)
        else:
            # No selection, align the entire line where the cursor is
            current_index = self.text.index(tk.INSERT)
            current_line = current_index.split('.')[0]

            # Get the text within the current line
            start = f'{current_line}.0'
            end = f'{current_line}.end'
            current_line_text = self.text.get(start, end)

            # Apply alignment to the current line
            self.text.tag_configure(f'align_{current_line}', justify=align)
            self.text.tag_add(f'align_{current_line}', start, end)

            # Update the current line text with alignment
            self.text.delete(start, end)
            self.text.insert(start, current_line_text, f'align_{current_line}')


           
        
        

        
        
    def create_color_frame(self):
        if self.picker_active:
            if self.color_picker is not None:
                self.color_picker.place_forget()
            self.picker_active = False
        else:
            if self.color_picker is None:
               self.color_picker = CTkColorPicker(width=500, command=self.ask_color, orientation='horizontal', corner_radius=5)
               
            self.color_picker.place(in_ = self.color_button, relx=1,rely=1.3, anchor='n')
            self.picker_active = True
        
        
    def ask_color(self, selected_color):
        self.text.configure(fg=selected_color)
        
        
    def change_spacing(self, selected_spacing):
        
        self.text.configure(spacing1=selected_spacing)
        self.spacing_button.configure(text=selected_spacing)
      
    def bold_text_test(self):
        sel_start, sel_end = self.get_selection_indices()
        if sel_start and sel_end:
            # Check if 'bold' tag is already applied
            is_bold_applied = 'bold' in self.text.tag_names(f'1.{sel_start}')
            for index in range(sel_start, sel_end):
                if is_bold_applied:
                    self.text.tag_remove('bold', f'1.{index}', f'1.{index + 1}')
                else:
                    self.text.tag_add('bold', f'1.{index}', f'1.{index + 1}')
            self.text.tag_configure('bold', font=(None, self.default_textfield_font_size, 'bold'))
        else:
            if 'bold' in self.styles:
                self.styles.remove('bold')
            else:
                self.styles.append('bold')
        self.update_text_style()

    def italic_text_test(self):
        sel_start, sel_end = self.get_selection_indices()
        if sel_start and sel_end:
            # Check if 'italic' tag is already applied
            is_italic_applied = 'italic' in self.text.tag_names(f'1.{sel_start}')
            for index in range(sel_start, sel_end):
                if is_italic_applied:
                    self.text.tag_remove('italic', f'1.{index}', f'1.{index + 1}')
                else:
                    self.text.tag_add('italic', f'1.{index}', f'1.{index + 1}')
            self.text.tag_configure('italic', font=(None, self.default_textfield_font_size, 'italic'))
        else:
            if 'italic' in self.styles:
                self.styles.remove('italic')
            else:
                self.styles.append('italic')
        self.update_text_style()

    def underline_text_test(self):
        sel_start, sel_end = self.get_selection_indices()
        if sel_start and sel_end:
            # Check if 'underline' tag is already applied
            is_underline_applied = 'underline' in self.text.tag_names(f'1.{sel_start}')
            for index in range(sel_start, sel_end):
                if is_underline_applied:
                    self.text.tag_remove('underline', f'1.{index}', f'1.{index + 1}')
                else:
                    self.text.tag_add('underline', f'1.{index}', f'1.{index + 1}')
            self.text.tag_configure('underline', font=(None, self.default_textfield_font_size, 'underline'))
        else:
            if 'underline' in self.styles:
                self.styles.remove('underline')
            else:
                self.styles.append('underline')
        self.update_text_style()



    def update_text_style(self):
        font_style = ' '.join(self.styles)
        self.text.configure(font=(self.font, self.default_textfield_font_size, font_style))

    def get_selection_indices(self):
        try:
            sel_start = int(self.text.index(tk.SEL_FIRST).split('.')[1])
            sel_end = int(self.text.index(tk.SEL_LAST).split('.')[1])
            return sel_start, sel_end
        except tk.TclError:
            return None, None
            
        
        
        
        
        
    def bold_text(self, style):
        
        self.styles = []
        self.styles.append(style)
        print(self.styles)
       
       
        
            
        try:
            self.selection_start = self.text.index('sel.first')
            self.selection_end = self.text.index('sel.last')
            self.text.tag_add('bold', self.selection_start, self.selection_end)
        except:
            self.selection_start = None
            self.selection_end = None

       
       
        if  not self.isBold and not self.isItalic and self.selection_start == None:
                 self.font_style = 'bold'
                 self.text.configure(font=(self.font, self.default_textfield_font_size, self.styles))
                 self.isBold = True
                 
        elif self.isBold:
                 self.font_style = None
                 self.text.configure(font=(self.font, self.default_textfield_font_size))
                 self.isBold = False
             
        elif self.isBold == True and self.isItalic == True and (self.selection_start and self.selection_end) is None:
                self.text.configure(font=(self.font, self.default_textfield_font_size, 'italic'))
                self.isBold = False
                
        elif self.isBold == False and  self.isItalic == False and (self.selection_start and self.selection_end) is not None:  
                self.text.tag_config('bold', font=(self.font, self.default_textfield_font_size, 'bold'))
                self.isBold = True
                
        elif self.isBold == False and self.isItalic == True and (self.selection_start and self.selection_end) is not None:
                self.text.tag_config('bold', font=(self.font, self.default_textfield_font_size, 'bold italic'))
                self.isBold = True
                
        elif self.isBold == True and (self.selection_start and self.selection_end) is not None:  
                self.text.tag_config('bold', font=(self.font, self.default_textfield_font_size))
                self.isBold = False
                self.text.tag_remove('bold', self.selection_start, self.selection_end)
                
        elif self.isBold == True and  self.isItalic == True and (self.selection_start and self.selection_end) is not None:  
                self.text.tag_config('bold', font=(self.font, self.default_textfield_font_size, 'italic'))
                self.isBold = False
                self.text.tag_remove('bold', self.selection_start, self.selection_end)
            
        

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
      

 
       
     