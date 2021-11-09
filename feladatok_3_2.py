import random
import math
szamok = []

alap = 10
for x in range(20):
    random_szam = random.randint(alap, 99)
    szamok.append(random_szam)
    alap = random_szam

szamok = []
for x in range(20):
    szamok.append(random.randint(10, 99))
szamok.sort()

szamok = []
also = 10
for x in range(20):
    szamok.append(random.randint(also, also + 89//20))
    also = szamok[x]

print(szamok)
