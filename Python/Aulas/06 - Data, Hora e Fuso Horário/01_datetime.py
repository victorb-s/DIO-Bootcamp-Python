import datetime

# Data selecionada (Ano - Mês - Dia)
data = datetime.date(2006, 7, 24)
print(data)

# Data do dia (Ano - Mês - Dia)
print(datetime.date.today())

# Data selecionada com hora - minuto - segundo
data_hora = datetime.datetime(2006, 7, 24, 10, 30, 20)
print(data_hora)

# Data do dia com hora - minuto - segundo
print(datetime.datetime.today())

# Hora selecionada
hora = datetime.time(10, 20, 0)
print(hora)