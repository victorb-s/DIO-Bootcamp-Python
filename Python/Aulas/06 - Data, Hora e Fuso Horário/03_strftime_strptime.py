from datetime import datetime

data_hora_atual = datetime.now()
data_hora_str = "10-20-2024 10:20"
mascara_ptbr = "%d/%m/%Y %a"
mascara_en = "%m-%d-%Y %H:%M"

# Cria uma string da data
print(data_hora_atual.strftime(mascara_ptbr))

# Cria um objeto data a partir da string
print(datetime.strptime(data_hora_str, mascara_en))