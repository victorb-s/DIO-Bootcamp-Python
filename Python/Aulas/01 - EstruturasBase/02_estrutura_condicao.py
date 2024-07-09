MAIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Você já pode tirar a CNH.")

else:
    print("Infelizmente você não atinge a idade mínima")

# ------------------------------------

if idade >= MAIOR_IDADE:
    print("Você já pode tirar a CNH.")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Infelizmente você não atinge a idade mínima")

# ------------------------------------

contaNormal = False
contaUniversitaria = True

saldo = 2000
saque = 500
chequeEspecial = 450

if contaNormal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + chequeEspecial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")
    
elif contaUniversitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    else:
        print("Não foi possível realizar o saque, saldo insuficiente!")

# ------------------------------------

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")