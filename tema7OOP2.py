# Ex 2:
### ABSTRACTION

from abc import ABC, abstractmethod

class FormaGeometrica(ABC):
    PI = 3.14


    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")

class Cerc(FormaGeometrica):
    def __init__(self, cerc):
        self.cerc = cerc

    def aria(self):
         return FormaGeometrica.PI * self.cerc * self.cerc

cerc = Cerc(7)
print(cerc.aria())
cerc.descrie()

### INHERITANCE

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.latura = latura

    def aria(self):
        return self.latura * self.latura

patrat = Patrat(15)
print(patrat.aria())
patrat.descrie()


### ENCAPSULATION

class Patrat(FormaGeometrica):
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.setter
    def latura(self, value):
        self.__latura = value

    @latura.deleter
    def latura(self):
        del self.__latura

    def aria(self):
        return self.__latura * self.__latura

class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.setter
    def raza(self, value):
        self.__raza = value

    @raza.deleter
    def raza(self):
        del self.__raza

    def aria(self):
        return FormaGeometrica.PI * self.__raza * self.__raza

patrat = Patrat(10)
print(patrat.latura)
patrat.latura = 20
print(patrat.aria())
patrat.descrie()

cerc = Cerc(10)
print(cerc.raza)
cerc.r = 20
print(cerc.aria())
cerc.descrie()

### POLYMORPHISM
class Patrat():
    def descrie(self):
        print("Eu am colturi")

class Cerc():
    def descrie(self):
        print("Eu nu am colturi")

patrat = Patrat()
cerc = Cerc()
for forma_geometrica in (cerc, patrat):
    forma_geometrica.descrie()
