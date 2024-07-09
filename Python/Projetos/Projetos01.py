# Solicita ao usuário que insira o consumo médio mensal de dados:

consumo = float(input("Informe o seu consumo médio mensal de dados (em GB): "))
plano_ideal = ""

# TODO: Crie uma Estrutura Condicional para verifica o consumo médio mensal 
if (consumo < 0):
  print("Insira um valor válido!")
  
elif (consumo > 0 and consumo <= 10):
  plano_ideal = "Plano Essencial Fibra - 50Mbps"
    
elif (consumo > 10 and consumo <= 20):
  plano_ideal = "Plano Prata Fibra - 100Mbps"
    
elif (consumo > 20):
  plano_ideal = "Plano Premium Fibra - 300Mbps"

else:
  print("Você não utiliza internet.")
  plano_ideal = "Plano Essencial Fibra - 50Mpbs, para você desfrutar da internet"
    
# TODO: Crie uma Função: recomendar_plano para receber o consumo médio mensal:

def recomendar_plano(consumo, plano_ideal):
  print(f"De acordo com seu consumo médio mensal de {consumo}GB, indicamos a você o plano: {plano_ideal}!")
  

# TODO: Retorne o plano de internet adequado:
# Chama a função recomendar_plano com o consumo inserido e imprime o plano recomendado:
recomendar_plano(consumo, plano_ideal)