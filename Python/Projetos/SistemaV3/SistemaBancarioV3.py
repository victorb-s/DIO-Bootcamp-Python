import textwrap
import os
from abc import ABC, abstractmethod
from datetime import datetime, timezone

class ContasIterador:
    def __init__(self, contas):
        self.contas = contas
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            conta = self.contas[self._index]
            return f"""\
            Agência:\t{conta.agencia}
            Número:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
            Saldo:\t\tR$ {conta.saldo:.2f}
        """
        except IndexError:
            raise StopIteration
        finally:
            self._index += 1

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
        self.indice_conta = 0

    def realizar_transacao(self, conta, transacao):
        if len(conta.historico.transacoes_do_dia()) >= 10:
            print("\n=== Você excedeu o número limite de transações diárias ===")
            return
        
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
    
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("\n=== Operação falhou! Você não tem saldo suficiente. ===")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True
        
        else:
            print("\n=== Operação falhou! O valor informado é inválido. ===")
            
        return False
    
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n=== Operação falhou! O valor informado é inválido. ===")
            return False
        
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero, limite, limite_saques):
        return cls(numero, cliente, limite, limite_saques)

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao for transacao in self.historico.transacoes
                if transacao["tipo"] == "Saque" # "Saque" == Saque.__name__
            ] 
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n=== Operação falhou! O valor do saque excede o limite. ===")

        elif(excedeu_saques):
            print("\nOperação falhou! Número máximo de saques excedido. ===")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now(timezone.utc).strftime("%d-%m-%Y %H:%M:%S")
            }
        )

    def gerar_relatorio(self, tipo_transacao=None):
        for transacao in self._transacoes:
            if (
                tipo_transacao is None
                or transacao["tipo"].lower() == tipo_transacao.lower()
            ):
                yield transacao

    def transacoes_do_dia(self):
        data_atual = datetime.now(timezone.utc).date()
        transacoes = []
        for transacao in self._transacoes:
            data_transacao = datetime.strptime(
                transacao["data"], "%d-%m-%Y %H:%M:%S"
            ).date()

            if data_atual == data_transacao:
                transacoes.append(transacao)
        return transacoes
        
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @property
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

def log_transacao(func):
    def envelope(*args, **kwargs):
        resultado = func(*args, **kwargs)
        print(f"{datetime.now(timezone.utc)}")
        return resultado

    return envelope

def menu():
    menu = """\n
    =========== MENU ===========
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNovo usuário
    [5]\tCriar Conta
    [6]\tListar Contas
    [7]\tSair
    --> """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n=== Cliente não possui conta! ===")
        return

    return cliente.contas[0]

def operacao(clientes, pergunta, op):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return
    
    valor = float(input(f"{pergunta}"))
    transacao = op(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

@log_transacao
def depositar(clientes):
    operacao(
        clientes,
        "Informe o valor do depósito: R$",
        Deposito
    )

    return "Tipo de transação: Depósito"

@log_transacao
def sacar(clientes):
    operacao(
        clientes=clientes,
        pergunta="Informe o valor do saque: R$",
        op=Saque
    )

    return "Tipo de transação: Saque"

@log_transacao
def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n=============== EXTRATO ===============")
    extrato = ""
    tem_transacao = False
    for transacao in conta.historico.gerar_relatorio():
        tem_transacao = True
        extrato += f"{transacao['tipo']}: R${transacao['valor']:.2f}\n{transacao['data']}\n"

    
    if not tem_transacao:
        extrato = "Não foram realizadas movimentações."
            

    print(extrato)
    print(f"\nSaldo:\tR$ {conta.saldo:.2f}")
    print("\n=======================================")
    return "Tipo de transação: Extrato"

@log_transacao
def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Já exsite cliente com esse CPF! ===")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(
        nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco
    )

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")
    return "Tipo de transação: Cadastrar Cliente"

@log_transacao
def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n=== Cliente não encontrado! ===")
        return
    
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta, limite=500, limite_saques=50)

    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")
    return "Tipo de transação: Criar Conta"

def listar_contas(contas):
    for conta in ContasIterador(contas):
        print("=" * 50)
        print(textwrap.dedent(str(conta)))

def main():
    os.system('cls')
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            resultado = depositar(clientes)
            print(resultado)

        elif opcao == "2":
            resultado = sacar(clientes)
            print(resultado)

        elif opcao == "3":
            resultado = exibir_extrato(clientes)
            print(resultado)

        elif opcao == "4":
            resultado = criar_cliente(clientes)
            print(resultado)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            resultado = criar_conta(numero_conta, clientes, contas)
            print(resultado)

        elif opcao == "6":
            listar_contas(clientes)

        elif opcao == "7":
            break

        else:
            print("\n=== Operação inválida, por favor, selecione novamente a operação desejada. ===")

main()