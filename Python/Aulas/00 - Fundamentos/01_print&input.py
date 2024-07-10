nome = input("Informe o seu nome: ") #String por padrão
idade = int(input('Informe a sua idade: '))

print(nome, idade)
print(f"O usuário {nome} possui {idade} anos")

print(nome, idade, end='... \n')
print(nome, idade, sep='+')
print(nome, idade, sep='&', end="... \n")
