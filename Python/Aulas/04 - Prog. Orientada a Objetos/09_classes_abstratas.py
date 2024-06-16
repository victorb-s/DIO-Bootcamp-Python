from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):  
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractmethod
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("TV Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("TV desligada!")

    @property
    def marca(self):
        return "LG"

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando ar-condicionado...")
        print("Ar-condicionado Ligado!")

    def desligar(self):
        print("Desligando ar-condicionado...")
        print("Ar-condicionado desligado!")

    @property
    def marca(self):
        return "Philco"

    # ERRO SEM ALGUM DAS DEFS POIS NÃO HÁ TODOS ELEMENTOS ABSTRATOS DA CLASSE PAI PRESENTES

controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)