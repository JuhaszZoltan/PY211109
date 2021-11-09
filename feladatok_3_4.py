import random
szamok = []

for x in range(50):
    szamok.append(random.randint(5, 49)* 2 + 1)

benne_van = szamok.__contains__(13)
if benne_van: print('tartalmazza a 13mat')
else: print('NEM tartalmazza a 13mat')

i = 0
while(i < len(szamok) and szamok[i] != 13):
    i += 1
if i < len(szamok): print('van')
else: print('nincs')