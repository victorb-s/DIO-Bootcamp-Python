def meu_decorador(funcao):
    def envelope():
        print("Antes da execução")
        funcao()
        print("Depois da execução")

    return envelope

@meu_decorador
def ola_mundo():
    print("Olá mundo!")

ola_mundo()