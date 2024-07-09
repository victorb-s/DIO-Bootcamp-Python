class Cachorro:
    # Inicializa a classe
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # Ocorre no fim das açoes, como falar
    def __del__(self):
        print("Removendo a instância da classe...")

    def falar(self):
        print("auau")

# def criar_cachorro():
#     c = Cachorro("Zeus", "Branco e Preto", False)
#     print(c.nome)

c = Cachorro("Chappie", "Caramelo")
c.falar()

print("Olá Mundo")
# Forçar delete
del c

print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
print("Olá Mundo")
