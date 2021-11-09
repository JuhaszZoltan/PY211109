import random

# 5db véletlen KÜLÖNBÖZŐ szám 1 és 10 között
sorsolt = []
futas = 0
while len(sorsolt) < 5:
    rnd = random.randint(1, 10)
    futas += 1
    if (not sorsolt.__contains__(rnd)):
        sorsolt.append(rnd)


print(sorsolt)
print(f'ennyiszer futott le a ciklus: {futas}')

# szamok = []
# for x in range(1, 11):
#     szamok.append(x)

# 2. megoldás (mindig ugyan annyiszor fut le a ciklus)
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for i in range(5):
    x = random.randrange(len(szamok))
    y = random.randrange(len(szamok))
    s = szamok[x]
    szamok[x] = szamok[y]
    szamok[y] = s

print(szamok)

sorsolt = []
for i in range(5):
    sorsolt.append(szamok[i])

print(sorsolt)

# 3. megoldás (beépített funkcióval)
szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(szamok)
random.shuffle(szamok)
print(szamok)

import numpy

# sorsolt = [szamok[0], szamok[1], szamok[2], szamok[3], szamok[4]]
# print(sorsolt)

szamok = numpy.resize(szamok, 5)
print(szamok)