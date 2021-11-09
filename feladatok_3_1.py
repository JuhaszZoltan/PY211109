import random

nevek = ['Elek', 'Béla', 'Zsuzsa', 'Szandra', 'Zoli', 'Csilla', 'Czezarina']

# egyesével kiírás ciklussal:
for nev in nevek:
    print(nev)

# alapértelmezett lista kiírás:
print(nevek)

# rendezés:
nevek.sort()
print(nevek)

szamok = []
for i in range(20):
    szamok.append(random.randint(50, 150))
szamok.sort()
print(szamok)

osszeg = 0
for szam in szamok:
    osszeg += szam
print(f'számok összege: {osszeg}')
print(f'számok átlaga: {osszeg/len(szamok)}')

nullara_vegzodok_szama = 0
for szam in szamok:
    if szam % 10 == 0: nullara_vegzodok_szama += 1
print(f'nullara végződő számok: {nullara_vegzodok_szama} db')
