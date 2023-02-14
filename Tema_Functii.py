### Exercitiul_1

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for
for i in range(len(masini)):
    print(f"Masina mea preferata este {masini[i]}")

# foreach
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    print(f"Masina mea preferata este {masina}")

# while
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
i = 0
while i < len(masini):
    print(f"Masina mea preferata este {masini[i]}")
    i += 1


### Exercitiul_2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for i in range(1,(len(masini)-1)):
    masini[i] = masini[i].upper()
else:
    print(masini)

### Exercitiul_3
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == 'Mercedes':
        print("Am gasit masina dorita de dvs")
        break
    else:
     print("Am gasit masina X.Mai cautam")


### Exercitiul_4
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Lastun" or "Trabant":
        continue
print(f"S-ar putea sa va placa masina {masina} ")


### Exercitiul_5
masini_vechi = []
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
for masina in masini:
    if masina == "Lastun" or masina == "Trabant":
        masini_vechi.append(masina)
        masini.remove(masina)
        masini.append("Tesla")
print(f"Modele vechi: {masini_vechi}")
print(f"Modele noi: {masini}")


### Exercitiul_6
pret_masini = {
    'Dacia' : 6800,
    'Latsun' : 500,
    'Opel' : 1100,
    'Audi' : 19000,
    'BMW' : 23000
}
for i, buget in pret_masini.items():
    if buget <= 15000:
        print(i, ' : ', pret_masini[i], 'euro')

for i, buget in pret_masini.items():
    if buget <= 15000:
        print(f'Pentru un buget de sub 15000 euro, puteti alege masina {i}. ')


### Exercitiul_7
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for i in numere:
     if i == 3:
        count += 1
print(count)


### Exercitiul_8
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
sum = 0
for i in numere:
    sum += i
print(sum)

### Exercitiul_9
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
max = numere[0]
for i in numere:
    if i > max:
        max = i
print(max)

### Exercitiul_10
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
numere_negative = []
for i in numere:
    numere_negative.append(-abs(i))
print(numere_negative)
















