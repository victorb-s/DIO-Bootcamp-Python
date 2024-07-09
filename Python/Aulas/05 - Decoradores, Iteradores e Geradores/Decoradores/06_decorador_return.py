def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Antes da execução")
        resultado = funcao(*args, **kwargs)
        print("Depois da execução")
        return resultado

    return envelope

@meu_decorador
def ola_mundo(nome):
    print(f"Olá mundo, eu sou {nome}!")
    return nome.upper()

resultado = ola_mundo("Victor")
print(resultado)