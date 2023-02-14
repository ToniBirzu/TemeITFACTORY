#Tema_2

####Exercitiul_1
# Variabila este un recipient caruia ii atribuim o valoare.
# Variabila este creata cand ii insusim o valoare, si fiecare dintre ele au un nume unic.

####Exercitiul 2
#string
marca = "Audi"
#int
an_fabricatie = 2008
#float
cai_putere = 239.5
#bool
neagra = True

print(f"Acest {marca} este anul {an_fabricatie} si are {cai_putere} hp")

####Exercitiul 3
print(type(marca))
print(type(an_fabricatie))
print(type(cai_putere))
print(type(neagra))

####Exercitiul 4
cai_putere = 239.5
cai_putere = round(cai_putere)
print(round(cai_putere))
print(cai_putere)
print(type(cai_putere))

####Exercitiul 5
#string
marca = "Audi"
print(f"Aceasta masina este {marca}")
#int
an_fabricatie = 2008
print(f"Este anul {an_fabricatie}" )
#float
cai_putere = 239.5
print(f"Are un pic de putere, mai exact {cai_putere}")
#bool
neagra = True
print(f"O fi neagra? {neagra}")

####EXercitiul 6
nume = "Moisa"
prenume = "Vlad"
print(f"{nume} {prenume} are {len(nume) + len(prenume)} caractere")

#####Exercitiul 7
lungimea = 7
latimea = 3
aria_dreptunghi = latimea * lungimea
print(f"Aria dreptunghiului este {aria_dreptunghi}")


#####Exercitiul 8
prop = "Coral is either the stupidest animal or the smartest rock"
print(prop.count(" the "))

####Exercitiul 9
prop = "Coral is either the stupidest animal or the smartest rock"
print(prop.count("the"))

####Exercitiul 10
prop = 'Coral is either the stupidest animal or the smartest rock'
assert prop == 'Coral is either the stupidest animal or the smartest rock'
print('fara numere')
assert prop == 'Coral'
print('asta e')

