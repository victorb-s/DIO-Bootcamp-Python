# Padrão Listas

frutas = ["Maçã", "Laranja", "Uva", "Pera"]
print(frutas[0]) # Primeiro elemento
print(frutas[-1], "\n") # Último elemento

# Listas aninhadas

matriz = [
    [1, "a", 3],
    ["b", 5, 6],
    [7, 8, "c"]
]

print(matriz[0]) # Primeria linha
print(matriz[0][0], "\n") # Primeira linha, primeiro elemento

# Utilizando For em listas 

carros = ['Gol', 'Celta', 'Palio']

for indice, carro in enumerate(carros):
    print(f'{indice}: {carro}')

# Utilizando Append

numeros = [1, 30, 21, 2, 9, 65, 34]
quadrados = []

for numero in numeros:
    quadrados.append(numero ** 2)

print(*quadrados)

# Utilizando Sort

linguagens = ["python", "js", "c", "java", "csharp"]
print(linguagens.sort(key=lambda x: len(x), reverse=True))
# Sort = Organizar alfabeticamente == sorted(lista, keys)
# Lambda = Função anônima
# x: len(x) = Organizar por número de letras
# Reverse = Organizar de trás pra frente

# Len conta tamanho da lista

print(len(linguagens))