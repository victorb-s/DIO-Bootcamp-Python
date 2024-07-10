arquivo = open(r"C:\Users\pegas\OneDrive\Documentos\Programação - Estudos\DIO\Bootcamp-Python\Python\Aulas\07 - Manipulando Arquivos\lorem.txt", "r")

print(arquivo.read()) # Ler todo conteúdo de uma vez
print(arquivo.readline()) # Ler linha a linha sem carregar na memória
print(arquivo.readlines()) # Carregar conteúdo em uma lista

while len(linha := arquivo.readline()):
    print(linha)

arquivo.close()