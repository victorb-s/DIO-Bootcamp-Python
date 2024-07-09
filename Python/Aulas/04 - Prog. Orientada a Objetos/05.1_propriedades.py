class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    # Property retorna valor
    def x(self):
        return self._x or 0
    
    @x.setter
    # Setter atribui valor a uma propriedade
    def x(self, valor):
        self._x += valor

    @x.deleter
    def x(self):
        self._x = 0

foo = Foo(10)
print(foo.x)

del foo.x
print(foo.x)

foo.x = 10
print(foo.x)