import pytz
from datetime import datetime

data = datetime.now(pytz.timezone('America/Sao_Paulo'))
data2 = datetime.now(pytz.timezone('America/Los_Angeles'))

print(data)
print(data2)