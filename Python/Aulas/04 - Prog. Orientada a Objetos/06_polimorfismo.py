import os
os.system('cls')

# len([10, 20, 30])

class Passaro:
    def voar(self):
        print("Voando...")

class Pardal(Passaro):
    def voar(self):
        super().voar()

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não pode voar.")


# FIXME: exemplo ruim do uso de herança para "ganhar" o método voar
class Aviao(Passaro):
    def voar(self):
        print("O avião está decolando...")

def plano_voo(obj):
    obj.voar()

p1 = Pardal()

plano_voo(p1)
plano_voo(Avestruz())
plano_voo(Aviao())