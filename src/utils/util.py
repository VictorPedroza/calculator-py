class Validatidate:
    @staticmethod
    def expression(expression):
        """Valida se a expressão é segura para avaliação"""
        characters = set('0123456789+-*/.%() ')
        return all(c in characters for c in expression)
    
    @staticmethod
    def format_result(result):
        """Formata o result para exibição"""
        if isinstance(result, float):
            if result.is_integer():
                return str(int(result))
            return f"{result:.10f}".rstrip('0').rstrip('.')
        return str(result)

class Operations:
    @staticmethod
    def percent(valor):
        return valor / 100
    
    @staticmethod
    def invert(valor):
        return -valor