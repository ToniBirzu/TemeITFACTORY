from tema7 import Cerc, Dreptunghi, Angajat, Cont

cerc = Cerc(12, "albastru")
cerc.descrie_cerc()
print(cerc.calculeaza_aria())
print(cerc.calculeaza_diametru())
print(cerc.calculeaza_circumferinta())

dreptunghi = Dreptunghi(10, 7, "rosu")
dreptunghi.descrie_dreptunghiul()
print(dreptunghi.calculeaza_aria())
print(dreptunghi.calculeaza_perimetru())
dreptunghi.schimba_culoarea("roz")
dreptunghi.descrie_dreptunghiul()

angajat = Angajat("Birzu", "Toni", 50000)
angajat.descrie_angajat()
print(angajat.nume_complet())
print(angajat.salariu_luna())
print(angajat.salariu_anual())
angajat.marime_salariu(7)
angajat.descrie_angajat()

cont = Cont("Birzu Toni", "RO1289", 78798)
cont.afisare_sold()
cont.debitare_cont(765)
cont.afisare_sold()
cont.creditare_cont(245)
cont.afisare_sold()