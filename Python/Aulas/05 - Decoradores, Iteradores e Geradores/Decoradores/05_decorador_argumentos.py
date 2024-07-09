def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da execução")
        funcao(*args, **kwargs)
        print("Depois da execução")

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo, eu sou {nome}!")

ola_mundo("Victor")