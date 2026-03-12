from tkinter import messagebox
from utils.util import Validatidate, Operations

class Logic:
    def __init__(self):
        self.expression = ""
        self.result = ""
        self.validation = Validatidate()
        self.operations = Operations()
        self.last_result = None
        
    def add_character(self, character):
        """Adiciona um Caractere à expressão"""
        self.expression += str(character)
        return self.expression
    
    def clean(self):
        """Limpa toda a expressão"""
        self.expression = ""
        self.last_result = None
        return self.expression
    
    def backspace(self):
        """Apaga o último character"""
        self.expression = self.expression[:-1]
        return self.expression
    
    def calc(self):
        """Calcula o result da expressão"""
        try:
            if not self.expression:
                return ""
            
            if not self.validation.expression(self.expression):  # Corrigido: validation
                raise ValueError("Expressão contém characters inválidos")
            
            result = eval(self.expression)
            self.result = self.validation.format_result(result)  # Corrigido: format_result
            self.last_result = self.result  # Corrigido: last_result
            self.expression = self.result
            return self.result
            
        except ZeroDivisionError:
            messagebox.showerror("Erro", "Divisão por zero não permitida")
            self.clean()
            return ""
        except Exception as e:
            messagebox.showerror("Erro", f"Expressão inválida: {str(e)}")
            self.clean()
            return ""
    
    def percent(self):
        """Calcula percent"""
        try:
            if self.expression:
                value = float(eval(self.expression))
                result = self.operations.percent(value)  # Corrigido: operations
                self.expression = str(result)
                return self.expression
        except:
            messagebox.showerror("Erro", "Não foi possível calcular percent")
            return self.expression
    
    def invert(self):
        """Inverte o sinal do último número"""
        try:
            if self.expression and self.expression[-1].isdigit():
                import re
                numbers = re.findall(r'-?\d+\.?\d*', self.expression)
                if numbers:
                    last_number = numbers[-1]
                    if last_number.startswith('-'):
                        new_number = last_number[1:]
                    else:
                        new_number = '-' + last_number
                    
                    self.expression = self.expression[:-len(last_number)] + new_number
                    return self.expression
        except:
            pass
        return self.expression