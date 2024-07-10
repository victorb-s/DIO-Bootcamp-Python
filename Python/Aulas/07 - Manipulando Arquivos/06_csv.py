import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

COLUNA_ID = 0
COLUNA_NOME = 1

try:
    with open(ROOT_PATH/'usuarios.csv', 'w', newline='', encoding='utf-8') as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(['ID', 'Nome'])
        writer.writerow(['1', 'Maria'])
        writer.writerow(['2', 'João'])

# Mesmos códigos abaixo, maneiras diferentes.

except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}")

try:
    with open(ROOT_PATH/'usuarios.csv', 'r', newline='', encoding='utf-8') as arquivo:
        reader = csv.reader(arquivo)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            print(f'ID: {row[COLUNA_ID]}')
            print(f'Nome: {row[COLUNA_NOME]}\n')


except IOError as exc:
    print(f"Erro ao criar o arquivo {exc}")

try:
    with open(ROOT_PATH/'usuarios.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['ID']}")
            print(f"Nome: {row['Nome']}\n")
except IOError as exc:
    print(f'Erro ao criar o arquivo. {exc}')