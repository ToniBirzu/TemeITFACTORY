### Exercitiul_1
# a
note_muzicale = ['do', 're', 'mi', 'fa', 'sol', 'la', 'si']
print(note_muzicale)
# b
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
# c
note_muzicale.reverse()
print(note_muzicale)

### Exercitiul_2
nr_do = note_muzicale.count('do')
print(f'do apare in lista de {nr_do} ori')

### Exercitiul_3
# prima metoda
lista_1 = [3, 1, 0, 2]
lista_2 = [6, 5, 4]
#lista_1.extend(lista_2)
print(lista_1)
# a doua metoda
lista_noua = lista_1 + lista_2
print(lista_noua)

### Exercitiul_4
lista_noua.sort()
print(lista_noua)
lista_noua.remove(0)
print(lista_noua)

### Exercitiul_5
lista_noua = [1, 2, 3, 4, 5, 6]
if len(lista_noua) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

### Exercitiul_6
lista_noua.clear()
print(lista_noua)
#del lista_noua[:] se poate si prin aceasta metoda

### Exercitiul_7
if len(lista_noua) == 0:
    print('Lista este goala')
else:
    print('Lista nu este goala')

### Exercitiul_8
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
elevii = dict1.keys()
print(elevii)

### Exercitiul_9
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
print(f'Ana a luat nota {dict1["Ana"]}')
print(f'Gigel a luat nota {dict1["Gigel"]}')
print(f'Dorel a luat nota {dict1["Dorel"]}')

### Exercitiul_10
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
dict1['Dorel'] = 6
print(dict1)

### Exercitiul_11
dict1 = {
    'Ana': 8,
    'Gigel': 10,
    'Dorel': 5
}
dict1.pop('Gigel')
print(dict1)
dict1['Ionica'] = 9
print(dict1)

### Exercitiul_12
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
#zile_sapt ={'luni', 'marti', 'miercuri', 'luni', 'joi', 'vineri', 'sambata', 'duminica'}
#print(zile_sapt)
# nu poti avea doua elemente identice intr un set;
# duplicatele nu sunt afisate.

### Exercitiul_13
## cu operatori de comparatie
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if 'sambata' and 'duminica' in zile_sapt:
    print(f'{True}')
else:
    print(f'{False}')

## cu functie
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
if weekend.issubset(zile_sapt):
    print(f'{True}')
else:
    print(f'{False}')

### Exercitiul_14
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.difference(weekend))
print(weekend.difference(zile_sapt))

### Exercitiul_15
zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
weekend = {'sambata', 'duminica'}
print(zile_sapt.intersection(weekend))
print(weekend.intersection(zile_sapt))