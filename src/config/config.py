import customtkinter as ctk

class Config:
    # Configurações da janela
    title = "Calculadora - By Victor Pedroza"
    width = 350
    height = 500  
    
    # Tema do CustomTkinter
    theme = "dark"
    primary_color = "#1f538d"
    secondary_color = "#2b2b2b"
    
    # Configurações de aparência
    ctk.set_appearance_mode(theme)
    ctk.set_default_color_theme("dark-blue")
    
    # Fontes
    font_title = ("Roboto", 40, "bold")
    font_display = ("Roboto", 32)
    font_button = ("Roboto", 18, "bold")
    
    # Botões da calculadora
    buttons = [
        ['C', '⌫', '%', '÷'],
        ['7', '8', '9', '×'],
        ['4', '5', '6', '−'],
        ['1', '2', '3', '+'],
        ['±', '0', '.', '=']
    ]
    
    # Mapeamento de operadores
    operations = {
        '÷': '/',
        '×': '*',
        '−': '-',
        '+': '+',
        '%': '%'
    }