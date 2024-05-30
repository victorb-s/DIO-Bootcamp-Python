nome = "guiLHermE"

print(nome.upper()) # Letras em maiúsculo
print(nome.lower()) # Letras em minúsculo
print(nome.title()) # Apenas primeira letra em maiúsculo

texto = "        Olá Mundo!   "

print(texto.strip()) # Corta os espaços antes e depois da string
print(texto.rstrip()) # Corta os espaços depois da string
print(texto.lstrip()) # Corta os espaços antes da string

menu = "Python"

print(menu.center(14, "-"))
print("-".join(menu))