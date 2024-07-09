import os
import textwrap 



# Variáveis ------------------------------------
SAQUES_DIARIOS = 3
AGENCIA = "0001"

saldo = 1000.00
limite_saque = 500.00
numero_saques = 0
numero_conta = 1

extrato = ""
usuarios = []
contas = []



# Funções do Menu ------------------------------------
def nomeMenu():
    menu_cabecalho = " Banco do Polvo "
    print(menu_cabecalho.center(30, "-"))

def menu():
    print("| [U] - Criar Usuário")
    print("| [C] - Criar Conta-corrente")
    print("| [D] - Depositar")
    print("| [S] - Sacar")
    print("| [E] - Extrato")
    print("| [L] - Listar Usuários")
    print("| [V] - Listas Contas")
    print("| [F] - Finalizar")



# Funções do Usuário ------------------------------------

def criar_usuario(usuarios):
    cpf = input("\n- Informe o seu CPF (APENAS NÚMEROS): ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Um usuário com esse CPF já está cadastrado! ===\n")
        return

    nome = input("- Informe o seu nome completo: ")
    data_nascimento = input("- Informe sua data de nascimento no formato (DD/MM/YYYY): ")
    endereco = input("- Informe o seu endereço (logradouro - nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome" : nome, "data_nascimento" : data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário cadastrado com sucesso! ===\n")

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def listar_usuarios(usuarios):
    if not usuarios:
        print("\n=== Não há usuários cadastrados. ===\n")
    else:
        print("\n---------- LISTA DE USUÁRIOS ----------\n")
        for usuario in usuarios:
            linha = f"""
                Nome:\t\t\t{usuario['nome']}
                CPF:\t\t\t{usuario['cpf']}
                Endereço:\t\t{usuario['endereco']}
                Data de Nascimento:\t{usuario['data_nascimento']}
            """
            print("=" * 80)
            print(textwrap.dedent(linha))
            print("=" * 80)
        print("-----------------------------\n") 



# Funções de Conta ------------------------------------

def criar_cc(agencia, numero_conta, usuarios):
    cpf = input("\n - Informe o CPF do usuário: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===\n")
        return {"agencia" : agencia, "numero_conta" : numero_conta, "usuario": usuario}
    
    print("\n=== Usuário não encontrado, fluxo criação de conta encerrada! ===\n")

def listar_contas(contas):
    if not contas:
        print("\n=== Não há usuários cadastrados. ===\n")
    else:
        print("\n---------- LISTA DE CONTAS ----------\n")
        for conta in contas:
            linha = f"""\
                Agencia:\t\t{conta['agencia']}
                Número da Conta:\t{conta['numero_conta']}
                Nome do Usuário:\t{conta['usuario']['nome']}
                CPF do Usuário:\t\t{conta['usuario']['cpf']}
            """
            print("=" * 80)
            print(textwrap.dedent(linha))
            print("=" * 80)
        print("-----------------------------\n") 



# Funções do Banco ------------------------------------

def depositar(valor_deposito, saldo, extrato, /):
    if (valor_deposito < 0):
        print("=== Valor inválido, por favor, tente novamente ===\n")

    else:
        saldo += valor_deposito
        print(f"=== O valor foi depositado na sua conta, saldo atual em conta: R${saldo:,.2f} ===\n")

        info_extrato = f"Você realizou um depósito de R${valor_deposito:,.2f}"
        extrato = extrato + info_extrato + "\n"

    return saldo, extrato

def sacar(*, saldo, valor_saque, extrato, limite_saque, numero_saques, saques_diarios):
    excedeu_saldo = valor_saque > saldo
    excedeu_limite = valor_saque > limite_saque
    excedeu_saques = numero_saques >= saques_diarios

    if excedeu_saldo:
        print("\n=== Não foi possível sacar! Você não tem saldo suficiente disponível! ===")

    elif excedeu_limite:
        print("\n=== Não foi possível sacar! O valor do saque excedeu o limite. ===")

    elif excedeu_saques:
        print("\n=== Não foi possível sacar! Número de saques excedido. ===")

    elif valor_saque > 0:
        saldo -= valor_saque
        print(f"=== Você sacou R${valor_saque} com sucesso!, saldo atual em conta: R${saldo:,.2f} ===\n")

        info_extrato = f"Você realizou um saque de R${valor_saque:,.2f}"
        extrato += info_extrato + "\n"

        numero_saques += 1

    else:
        print("\n=== Não foi possível sacar! O valor de saque é invalido. ===")

    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato ):
    if not extrato:
        print("=== Não foram realizadas movimentações. ===\n")
    else:
        print("\n---------- EXTRATO ----------")
        print(extrato)
        print(f"Saldo: R${saldo:,.2f}")
        print("-----------------------------\n") 



# Rodar funções ------------------------------------

def escolha(saldo, limite_saque, numero_saques, SAQUES_DIARIOS, extrato, numero_conta):
    while True:
        nomeMenu()
        menu()
        opcao = input("=> ")
        match(opcao):
            case "u" | "U" | "Criar Usuario":
                criar_usuario(usuarios)

            case "c" | "C" | "Criar conta":
                conta = criar_cc(AGENCIA, numero_conta, usuarios)

                if conta:
                    contas.append(conta)
                    numero_conta += 1
 
            case "d" | "D" | "depositar" | "Depositar":
                valor_deposito = float(input("\nInforme o valor que deseja depositar: R$"))
            
                saldo, extrato = depositar(valor_deposito, saldo, extrato)

            case "s" | "S" | "sacar" | "Sacar":
                valor_saque = float(input("\nInsira o valor que seseja sacar: R$")) 

                saldo, extrato = sacar(
                    saldo = saldo,
                    valor_saque = valor_saque,
                    extrato = extrato,
                    limite_saque = limite_saque,
                    numero_saques = numero_saques,
                    saques_diarios = SAQUES_DIARIOS,
                )

            case "e" | "E" | "extrato" | "Extrato":
                exibir_extrato(saldo, extrato=extrato)

            case "l" | "L" | "Listar Usuarios": 
                listar_usuarios(usuarios)

            case "v" | "V" | "Listar Contas":
                listar_contas(contas)

            case "f" | "F" | "finalizar" | "Finalizar":
                print("\n=== Programa encerrado! ===")
                break

            case __:
                print("=== Insira uma opção válida, por favor. ===\n")



# Base da execução ------------------------------------     
def main():
    os.system('cls')
    escolha(saldo, limite_saque, numero_saques, SAQUES_DIARIOS, extrato, numero_conta)

if __name__ == '__main__':
    main()