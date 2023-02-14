### Exercitiul_1
class Cerc:
    raza = 0
    culoare = None


    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    def descrie_cerc(self):
        print(f" Culoare: {self.culoare}" 
              f" Raza: {self.raza}")

    def calculeaza_aria(self):
        return 3.14 * (self.raza ** 2)

    def calculeaza_diametru(self):
        return 2 * self.raza

    def calculeaza_circumferinta(self):
        return 2 * 3.14 * self.raza


### Exercitiul_2
class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descrie_dreptunghiul(self):
        print(f" Lungime:{self.lungime}"
              f" Latime:{self.latime}"
              f" Culoare:{self.culoare}")

    def calculeaza_aria(self):
        return self.lungime * self.latime

    def calculeaza_perimetru(self):
        return 2 * (self.lungime + self.latime)

    def schimba_culoarea(self, noua_culoare):
        self.culoare = noua_culoare

### Exercitiul_3
class Angajat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie_angajat(self):
        print(f" Nume:{self.nume}"
              f" Prenume:{self.prenume}"
              f" Salariu:{self.salariu}")

    def nume_complet(self):
        return f" {self.nume} {self.prenume}"

    def salariu_luna(self):
        return self.salariu / 12

    def salariu_anual(self):
        return self.salariu

    def marime_salariu(self, procent):
        self.salariu += self.salariu * (procent/100)

### Exercitiul_4
class Cont:
    titular_cont = None
    iban = None
    sold = 0

    def __init__(self, titular_cont, iban, sold):
        self.titular_cont = titular_cont
        self.iban = iban
        self.sold = sold

    def afisare_sold(self):
        print(f" Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei")

    def debitare_cont(self, suma):
        self.sold -= suma

    def creditare_cont(self, suma):
        self.sold += suma

