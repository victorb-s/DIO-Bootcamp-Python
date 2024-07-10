arquivo = open(r"C:\Users\pegas\OneDrive\Documentos\Programação - Estudos\DIO\Bootcamp-Python\Python\Aulas\07 - Manipulando Arquivos\teste.txt", "w")

arquivo.write("Escrevendo dados em um novo arquivo.") # Escreve uma string grande de uma vez só
arquivo.writelines(["\n", "escrevendo ", "um ", "novo ", "texto "]) # Escreve strings iterando elas

arquivo.close()