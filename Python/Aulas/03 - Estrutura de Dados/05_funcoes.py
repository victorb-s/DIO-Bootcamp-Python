def exibir_poema(data_extenso, *versos, **dicionario):
    texto = "\n".join(versos)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in dicionario.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Terça-Feira, 28 de Maio de 2024.",
    "Zen Of Python",
    "Beatiful is better than ugly",
    autor = "Tim Peters",
    ano = 1999,
)

print("----------------------")

# Parâmetros posicionais e nomeados

# Antes da / = Apenas por posição
# Depois da / = Posição ou nomeação
# Depois do * = Apenas por nomeação
def criar_carro(modelo, ano, /, placa, marca, *, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro(
    "Palio", 1999,
    "ABC-1234", marca="Fiat",
    motor="1.0", combustivel="Gasolina"
)

print("----------------------")

# Função como objeto de primeira classe

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def mostrar_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

mostrar_resultado(10, 10, somar)
mostrar_resultado(10, 10, subtrair)

print("----------------------")

