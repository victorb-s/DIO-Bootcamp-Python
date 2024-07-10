from datetime import datetime, timedelta
from pytz import timezone

tipo_carro = "P" # P, M, G
tempo_pequeno = 1440
tempo_medio = 45
tempo_grande = 60

data_atual = datetime.now()
fuso_horario = timezone('America/Sao_Paulo')

data_atual_brasil = data_atual.astimezone(fuso_horario)

if tipo_carro == "P":
    data_estimada = data_atual_brasil + timedelta(minutes=tempo_pequeno)

    data_atual_brasil = data_atual_brasil.strftime("%d/%m/%Y %H:%M")
    data_estimada = data_estimada.strftime("%d/%m/%Y %H:%M")

    print(f'O carro chegou: {data_atual_brasil} e ficará pronto às {data_estimada}')
    
elif tipo_carro == "M":
    data_estimada = data_atual_brasil + timedelta(minutes=tempo_medio)

    data_atual_brasil = data_atual_brasil.strftime("%d/%m/%Y %H:%M")
    data_estimada = data_estimada.strftime("%d/%m/%Y %H:%M")

    print(f'O carro chegou: {data_atual_brasil} e ficará pronto às {data_estimada}')

else:
    data_estimada = data_atual_brasil + timedelta(minutes=tempo_grande)

    data_atual_brasil = data_atual_brasil.strftime("%d/%m/%Y %H:%M")
    data_estimada = data_estimada.strftime("%d/%m/%Y %H:%M")

    print(f'O carro chegou: {data_atual_brasil} e ficará pronto às {data_estimada}')