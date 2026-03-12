import customtkinter as ctk
from config.config import Config
from service.logic import Logic

class Interface:
    def __init__(self):
        self.window = ctk.CTk()
        self.logic = Logic()
        self.result = ctk.StringVar()
        
        self.config_window()
        self.start_interface()
        
    def config_window(self):
        """Configura a janela principal"""
        self.window.title(Config.title)
        self.window.geometry(f"{Config.width}x{Config.height}")  # Corrigido: height
        self.window.resizable(False, False)
        
        # Centralizar a janela
        self.window.update_idletasks()
        width_window = self.window.winfo_screenwidth()
        height_window = self.window.winfo_screenheight()  # Corrigido: height
        x = (width_window - Config.width) // 2
        y = (height_window - Config.height) // 2  # Corrigido: height
        self.window.geometry(f"+{x}+{y}")
        
    def start_interface(self):
        """Cria todos os elementos da interface"""
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)
        self.window.grid_rowconfigure(1, weight=3)
        
        self.init_display()
        self.generate_buttons()
        
    def init_display(self):
        """Cria o display da calculadora"""
        display_frame = ctk.CTkFrame(self.window)
        display_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_rowconfigure(0, weight=1)
        
        # Display principal
        self.display = ctk.CTkLabel(
            display_frame,
            textvariable=self.result,
            font=Config.font_display,
            anchor="e",
            height=80,
            corner_radius=10
        )
        self.display.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
        
        # Label para mostrar operação atual
        self.operation = ctk.CTkLabel(
            display_frame,
            text="",
            font=("Roboto", 12),
            anchor="e",
            text_color="gray"
        )
        self.operation.grid(row=1, column=0, padx=10, pady=(0,5), sticky="ew")
        
    def generate_buttons(self):
        """Cria os botões da calculadora"""
        button_frames = ctk.CTkFrame(self.window)
        button_frames.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")
        
        # Configurar grid
        for i in range(5):
            button_frames.grid_rowconfigure(i, weight=1)
        for i in range(4):
            button_frames.grid_columnconfigure(i, weight=1)
        
        # Criar botões
        for i, line in enumerate(Config.buttons):
            for j, text_button in enumerate(line):
                self.create_button(button_frames, text_button, i, j)
                
    def create_button(self, parent, text, line, column):
        """Cria um botão individual"""
        
        # Configurar estilo baseado no tipo
        if text in ['C', '⌫']:
            fg_color = "#8B0000"
            hover_color = "#A52A2A"
        elif text in ['÷', '×', '−', '+', '%', '=']:
            fg_color = Config.primary_color
            hover_color = "#2a6d9c"
        elif text == '±':
            fg_color = "#4A4A4A"
            hover_color = "#5A5A5A"
        else:
            fg_color = Config.secondary_color
            hover_color = "#3A3A3A"
        
        if text == '=':
            fg_color = "#0066CC"
            hover_color = "#0077EE"
        
        button = ctk.CTkButton(
            parent,
            text=text,
            font=Config.font_button,
            fg_color=fg_color,
            hover_color=hover_color,
            height=60,
            corner_radius=8,
            command=lambda: self.click_button(text)
        )
        
        # Botão 0 ocupa 2 colunas
        if text == '0':
            button.grid(row=line, column=column, columnspan=2, padx=2, pady=2, sticky="nsew")
        else:
            button.grid(row=line, column=column, padx=2, pady=2, sticky="nsew")
        
    def click_button(self, value):
        """Processa o clique em um botão"""
        
        if value not in ['C', '⌫', '=']:
            self.operation.configure(text=f"Operação: {self.logic.expression}")
        
        if value == 'C':
            new_expression = self.logic.clean()
            self.operation.configure(text="")
            
        elif value == '⌫':
            new_expression = self.logic.backspace()
            
        elif value == '=':
            new_expression = self.logic.calc()
            
        elif value == '%':
            new_expression = self.logic.percent()
            
        elif value == '±':
            new_expression = self.logic.invert()
            
        else:
            # Converter operadores visuais
            if value in Config.operations:
                real_value = Config.operations[value]
            else:
                real_value = value
                
            new_expression = self.logic.add_character(real_value)
        
        self.result.set(new_expression)
        
        if value == '=' and self.logic.last_result:
            self.operation.configure(
                text=f"Resultado: {self.logic.last_result}"
            )
    
    def start(self):
        """Inicia a aplicação"""
        self.window.mainloop()