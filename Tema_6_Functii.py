### Exercitiul_1
def suma(numarul1, numarul2):
    return numarul1 + numarul2
print(suma(7, 17))

### Exercitiul_2
def este_nr_par_impar(numar):
    if numar % 2 == 0:
        return True
    else:
        return False
print(este_nr_par_impar(4))

### Exercitiul_3
def nr_total_caractere(nume, prenume, nume_mijlociu):
    caracter = 0
    for litera in nume.lower() + prenume.lower() + nume_mijlociu.lower():
        caracter += 1
    return f"Numarul total de caractere este {caracter}"
print(nr_total_caractere("Birzu", "Mihai", "Antoniu"))

### Exercitiul_4
def aria_dreptunghiului(lungime, latime):
    return lungime * latime
print(aria_dreptunghiului(9, 7))

### Exercitiul_5
def aria_cercului(raza2, pi = 3.14159):
    return pi * raza2 ** 2
print(aria_cercului(17))

### Exercitiul_6
def exista_caracter(caracter):
    for caracterul_x in caracter:
       if 't' in caracterul_x:
        return "Cuvantul contine acel caracter"
       else:
        return "Cuvantul nu contine acel caracter"
print(exista_caracter("tren"))

### Exercitiul_7
def count_lower_upper(cuvant):
    nr_caractere_lower = 0
    nr_caractere_upper = 0
    for litera in cuvant:
        if litera.islower():
            nr_caractere_lower += 1
        elif litera.isupper():
             nr_caractere_upper += 1
    print(f"Nr de caractere lower este {nr_caractere_lower} si nr caractere upper este {nr_caractere_upper}")
count_lower_upper("AlAbAlA")

### Exercitiul_8
def lista_numere_pozitive(numere):
    lista_numere_pozitive = []
    for numar in numere:
        if numar > 0:
            lista_numere_pozitive.append(numar)
    return lista_numere_pozitive
print(lista_numere_pozitive([- 2, 7, 10, - 6]))

### Exercitiul_9
def numere(numar1, numar2):
    if numar1 > numar2:
        print(f"Primul numar {numar1} este mai mare decat al doilea numar {numar2}")
    elif numar1 < numar2:
        print(f"Al doilea numar {numar2} este mai mare decat primul numar {numar1}")
    else:
        print("Numerele sunt egale")
numere(7, 5)


### Exercitiul_10
def numere_set(numar, set_numere):
    if numar not in set_numere:
        print("Am adaugat numarul nou in set")
        return True
    else:
        print("Nu am adaugat numarul in set. Acesta exista deja")
        return False
print(numere_set(7, {2, 3, 5, 6, 7}))





