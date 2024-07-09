class Estudante:
    # Variáveis de classe referem-se à todos os objetos criados a partir da classe
    escola = "DIO"

    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)

# Variáveis de instância são específicos à cada objeto criado, sem alterar nos demais objetos
aluno_1 = Estudante("Guilherme", 321412)
aluno_2 = Estudante("Giovanna", 421351)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python"
aluno_1.matricula = 364432
mostrar_valores(aluno_1, aluno_2)
