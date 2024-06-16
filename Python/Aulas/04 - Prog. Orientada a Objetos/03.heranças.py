# Herança Simples
class A:
    pass

class B(A):
    pass

# --------------------------------

class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor...")
        print("Motor inicializado!")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'}")

moto = Motocicleta("Vermelho", "XXXXX-010", 2)
print(moto)
moto.ligar_motor()
print("\n")

carro = Carro("Branco", "XDXDX-100", 4)
print(carro)
carro.ligar_motor()
print("\n")

caminhao = Caminhao("Roxo", "DDDDD-001", 8, False)
print(caminhao)
caminhao.ligar_motor()
caminhao.esta_carregado()
print("\n")

# Herança múltipla

class Q:
    pass

class W:
    pass

class E(Q, W):
    pass

# --------------------------------

class Animal:
    def __init__(self, numero_patas):
        self.numero_patas = numero_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)

class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, numero_patas):
        print(Ornitorrinco.__mro__)

        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, numero_patas=numero_patas)

gato = Gato(numero_patas=4, cor_pelo="Preto")
print(gato)

print("\n")

ornitorrinco = Ornitorrinco(numero_patas=4, cor_pelo="Azul", cor_bico="Laranja")
print(ornitorrinco)