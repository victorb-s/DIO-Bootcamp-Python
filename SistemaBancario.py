import os

saldo = 1000.00
limite_saque = 500.00
numero_saques = 0
saques_diarios = 3
extrato = ""

def nomeMenu():
    menu_cabecalho = " Menu do Banco "
    print(menu_cabecalho.center(20, "-"))

def menu():
    print("| d - Depositar")
    print("| s - Sacar")
    print("| e - Extrato")
    print("| f - Finalizar")

def escolha(saldo, limite_saque, numero_saques, saques_diarios, extrato):
    while True:
        menu()
        opcao = input("Escolha uma ação para realizar: ")
        match(opcao):
            case "d" | "D" | "depositar" | "Depositar":
                valor_deposito = float(input("\nInforme o valor que deseja depositar: R$"))
                if(valor_deposito < 0):
                    print("Valor inválido, por favor, tente novamente\n")
                else:
                    saldo += valor_deposito
                    print(f"O valor foi depositado na sua conta, saldo atual em conta: R${saldo:,.2f}\n")

                    info_extrato = f"Você realizou um depósito de R${valor_deposito:,.2f}"
                    extrato = extrato + info_extrato + "\n"
                continue
            
            case "s" | "S" | "sacar" | "Sacar":
                if(numero_saques < saques_diarios):
                    valor_saque = float(input("\nInsira o valor que seseja sacar: R$"))
                    if(valor_saque < 0):
                        print("Valor inválido, por favor, tente novamente\n")

                    elif(valor_saque > limite_saque):
                        print("O valor deste saque ultrapassou o limite de R$500,00, por favor tente novamente.")

                    elif(valor_saque < saldo and valor_saque <= limite_saque):
                        saldo -= valor_saque
                        print(f"Você retirou o valor com sucesso! Saldo atual em conta: R${saldo:,.2f}\n")
                        numero_saques += 1

                        info_extrato = f"Você realizou um saque de R${valor_saque:,.2f}"
                        extrato = extrato + info_extrato + "\n"

                    else:
                        print("Você não tem saldo suficiente para realizar este saque!\n")

                else:
                    print("O limite de saques diários foi atingido!\n")
                continue

            case "e" | "E" | "extrato" | "Extrato":
                if not extrato:
                    print("Não foram realizadas movimentações.\n")
                else:
                    print("\n---------- EXTRATO ----------")
                    print(extrato)
                    print(f"Saldo: R${saldo:,.2f}")
                    print("-----------------------------")



            case "f" | "F" | "finalizar" | "Finalizar":
                print("\nPrograma encerrado!")
                break

            case __:
                print("Insira uma opção válida, por favor.\n")
                continue
            
def main():
    os.system('cls')
    nomeMenu()
    escolha(saldo, limite_saque, numero_saques, saques_diarios, extrato)

if __name__ == '__main__':
    main()