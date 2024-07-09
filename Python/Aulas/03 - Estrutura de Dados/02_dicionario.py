pessoa = {"nome": "Guilherme", "idade": 28}
pessoa["telefone"] = "3333-1234"

print(pessoa["nome"])

# Dicionário aninhado

contatos = {
    "victorb.santos15@gmail.com": {"nome" : "Victor", "telefone" : "4002-8922"},
    "pegasus02xd@gmail.com": {"nome" : "Ronaldo", "telefone" : "4022-0289"},
    "pegasus03xd@gmail.com": {"nome" : "André", "telefone" : "9820-2204"},
    "victor@exemplo.com": {"nome" : "Barbosa", "telefone" : "8922-4002"},
}

print(contatos["victorb.santos15@gmail.com"]["telefone"])

# Aninhado utilizando for

for chave, valor in contatos.items():
    print(chave, valor)

# Métodos

exemplo = {

}

# Adicionar chaves
exemplo.fromkeys(["nome", "telefone"], "vazio")

# Procurar uma chave no dict, caso não exista, retorna vazio
print(contatos.get("victorb.santos15@gmail.com", {}))

# Remove uma chave no dict, caso não exista, retorna vazio
print(contatos.pop("victorb.santos15@gmail.com", "Não encontrou"))

# Adicionar um novo valor caso ele não exista:

contato = {"nome": "Guilherme", "telefone" : "3333-2221"}

contato.setdefault("idade", 28)
print(contato)

contatos.update({"victorb.santos15@gmail.com" : {"nome" : "Vec"}})
# Atualiza uma informação mas também adiciona caso não exista a chave

# Remover itens

del contatos["victor@exemplo.com"]["telefone"]
del contatos["victor@exemplo.com"]