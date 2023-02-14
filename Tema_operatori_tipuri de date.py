### Exercitiul_1
'''afirmatia if else este folosita pentru a executa
atat partea adevarata dar si cea falsa dintr o
anumita conditie. Daca conditia este adevarata, codul if se executa,
daca conditia if este falsa, atunci codul else se executa.'''

### Exerciutiul_2
x = 2
if type(x) == int and x > 0:
    print(f'{x} este numar natural')
else:
    print(f'{x} nu este numar natural')

### Exercitiul_3
x = 2
if x > 0:
    print(f'{x} este numar pozitiv')
elif x == 0:
    print(f'{x} este numar neutru')
else:
    print(f'{x} este numar negativ')

### Exercitiul_4
x = 2
if -2 < x < 13:
    print(f'{x} este intre -2 si 13')
elif x == -2 or x == 13:
    print(f"X este egal cu {x} ")
else:
    print(f'{x} nu corespunde')

### Exercitiul_5
x = 3
y = 10
if (abs(x - y)) < 5:
    print(f'diferenta dintre {x} si {y} este mai mica decat 5')
elif (abs(x - y)) > 5:
    print(f'diferenta dintre {x} si {y} este mai mare decat 5')
else:
    print(f'diferenta dintre {x} si {y} este egala cu 5')


### Exercitiul_6
x = 17
if not(x >= 5 and x <= 27):
    print('Nu este in acest interval')
else:
    print('Este in acest interval')

### Exercitiul_7
x = 17
y = 8
if x < y:
    print(f'{x} este mai mic decat {y}')
elif x > y:
    print(f'{x} este mai mare decat {y}')
else:
    print(f'{x} este egal cu {y}')

### Exerctiul_8
x = 10
y = 17
z = 10
if x == y == z:
    print('Acest triunghi este echilateral')
elif x == y or x == z or y == z:
    print('Acest triunghi este isoscel')
else:
    print('Este un triunghi oarecare')

### Exercitiul_9
vocala= str(input('Alege o vocala'))
vocale = 'AaEeIiOoUu'
if vocala in vocale:
    print('Ai ales bine!')
else:
    print('Mai incearca')

### Exrcitiul_10
nota = float(input("Introdu o nota din sistemul romanesc"))
if 9 < nota <= 10:
    print('Nota A in sistemul american')
elif 8 < nota <= 9:
    print('Nota B in sistemul american')
elif 7 < nota <= 8:
    print('Nota C in sistemul american')
elif 6 < nota <= 7:
    print('Nota D in sistem american')
elif 4 < nota <= 7:
    print('Nota E in sistem american')
elif 1 <= nota <= 4:
    print('Nota F in sistem american')
else :
    print('Introduce un numar intre 1 si 10')

