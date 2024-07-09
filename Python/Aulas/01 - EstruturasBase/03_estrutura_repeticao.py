texto = input("Informe um texto:" )
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

# -----------------------------------

for numero in range(0, 11):
    print(numero, end="\n")

for numero in range(0, 51, 5):
    print(numero, end="\n")
    
# -----------------------------------

while True:
    numeroRep = int(input("Informe um número: "))

    if numeroRep == 10:
        print("Saindo...")
        break
    
    if numeroRep % 2 == 0:
        print(numeroRep)
        continue