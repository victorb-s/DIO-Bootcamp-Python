print(set([1, 2, 3, 1, 3, 4]))
# Set remove itens repetidos

print(set(("Palio", "Gol", "Celta", "Palio")))

# Conjunto para Lista
numeros = {1, 2, 3, 4}
numeros = list(numeros)

print(numeros[0])

# Uso do For
carros = {"Gol", "Celta", "Palio"}

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Operações de conjuntos

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.union(conjunto_b)) # Juntar os elementos diferentes e iguais
print(conjunto_a.intersection(conjunto_b)) # Selecionar os números iguais

print(conjunto_a.difference(conjunto_b)) # Números de A que são diferentes de B
print(conjunto_b.difference(conjunto_a)) # Números de B que são diferentes de A
print(conjunto_a.symmetric_difference(conjunto_b)) # Numéros de A e B que são diferentes de AB

print(conjunto_a.issubset(conjunto_b)) # Todos elementos de A estão em B
print(conjunto_a.issuperset(conjunto_b)) # Todos elementos de B estão em A
print(conjunto_a.isdisjoint(conjunto_b)) # Nenhum elemento pertence ao outro

conjunto_a.add(25)
print(conjunto_a)

conjunto_b.clear()
print(conjunto_b)