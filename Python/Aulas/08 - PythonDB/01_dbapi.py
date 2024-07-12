import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "meu_banco.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(100))"
    )


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


inserir_registro(conexao, cursor, 'Gabriel', 'kgf@etepd.com')


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome=?, email=? WHERE id=?;", data)
    conexao.commit()


atualizar_registro(conexao, cursor, 'Victor Barbosa', 'vbs3@cesar.school', 1)
atualizar_registro(conexao, cursor, 'Isabel Fernandes', 'isabel.oliveira.2022@etepd.com', 2)


def remover_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id=?;", data)
    conexao.commit()


remover_registro(conexao, cursor, 3)


def adicionar_muitos(conexao, cursor, dados):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", dados)
    conexao.commit()


dados = [
    ('Pedro', 'pedro@exemplo.com'),
    ('João', 'joao@exemplo.com'),
    ('Levi', 'levi@exemplo.com'),
    ('Lucas', 'lucas@exemplo.com'),
]

adicionar_muitos(conexao, cursor, dados)

# Outra forma: (Mais demorada)
# for cliente in dados:
#     inserir_registro(conexao, cliente, cliente[0], cliente[1])


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT * FROM clientes WHERE id=?;", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

cliente = recuperar_cliente(cursor, 1)
print(dict(cliente))
print(cliente["id"], cliente["nome"], cliente["email"])

print(f'Seja bem vindo ao sistema, {cliente["nome"]}')
