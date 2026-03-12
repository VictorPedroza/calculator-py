# 🧮 Calculadora Moderna com CustomTkinter

Uma calculadora elegante e funcional desenvolvida em Python com interface gráfica moderna utilizando CustomTkinter.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![CustomTkinter](https://img.shields.io/badge/CustomTkinter-5.2.0-green)
![License](https://img.shields.io/badge/license-MIT-orange)

## 📸 Screenshots

## ✨ Funcionalidades

- ✅ **Operações básicas**: adição, subtração, multiplicação e divisão
- ✅ **Porcentagem**: cálculo rápido de porcentagens
- ✅ **Inversão de sinal**: botão `±` para alternar entre positivo/negativo
- ✅ **Backspace**: botão `⌫` para apagar o último caractere
- ✅ **Limpar tudo**: botão `C` para resetar a calculadora
- ✅ **Design moderno**: interface com cantos arredondados e efeitos hover
- ✅ **Tema dark**: visual elegante e agradável
- ✅ **Validação de erros**: tratamento para divisão por zero e expressões inválidas
- ✅ **Display informativo**: mostra a operação atual e o resultado

## 🚀 Tecnologias Utilizadas

- **Python 3.7+**: Linguagem de programação principal
- **CustomTkinter**: Biblioteca para interface gráfica moderna
- **Tkinter**: Base para a interface (já incluso no Python)

## 📋 Pré-requisitos

- Python 3.7 ou superior instalado
- pip (gerenciador de pacotes do Python)

## 🔧 Instalação

1. **Clone o repositório**
```bash
git clone https://github.com/VictorPedroza/calculator-py.git
cd calculadora-ctk
```

2. **Crie o Ambiente Virtual (Recomendado)**
```
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. **Instale as dependências**
```
pip install -r requirements.txt
```
- Verifique as dependências [AQUI](requirements.txt)

4. **Execute o Projeto**
```
python src/main.py
```

## 📁 Estrutura do Projeto
```
calculator-py/
│
├── src/                     # Diretório principal
│   ├── config/              # Configurações e constantes
│   │   └── config.py
│   ├── interface/           # Interface gráfica
│   │   └── interface.py
│   ├── service/             # Lógica de negócio
│   │   └── logic.py
│   └── main.py              # Arquivo principal de execução
├── utils/                   # Utilitários e funções auxiliares
│   └── util.py
├── .gitignore               # Arquivos ignorados pelo Git
├── LICENSE                  # Licença do projeto
├── README.md                # Documentação
└── requirements.txt         # Dependências do projeto
```

## 🎯 Como Usar
Operações Básicas

1. Clique nos números para formar sua expressão

2. Use os operadores (+, −, ×, ÷) para realizar operações

3.  Pressione = para ver o resultado

4.  Use C para limpar tudo ou ⌫ para apagar o último dígito

Funcionalidades Especiais

- **%:** Calcula a porcentagem do valor atual

- **±:** Inverte o sinal do número (positivo/negativo)

- **. :** Adiciona ponto decimal para números não inteiros


## ⚙️ Personalização

Você pode personalizar a calculadora editando o arquivo `src/config/config.py`:

Exeplo:
```
# Alterar tema (dark, light, system)
theme = "dark"

# Mudar cores principais
primary_color = "#1f538d"  
secondary_color = "#2b2b2b"  

# Ajustar tamanho da janela
width = 350
height = 500
```
## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENCE](LICENSE) para mais detalhes.