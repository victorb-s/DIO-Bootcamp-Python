class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento

    @property
    def nome(self):
        return self._nome
    
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento
    
    # Código padrão de outras linguagens
    def get_nome(self):
        return self._nome
    
    def get_idade(self):
        return 2024 - self._ano_nascimento
    
pessoa = Pessoa("Victor", 2006)
print(f"Nome: {pessoa.nome}\nIdade: {pessoa.idade}")

# Código padrão de outras linguagens
print(f"Nome: {pessoa.get_nome}\nIdade: {pessoa.get_idade}")