import random as rnd

TIPPEK_SZAMA = 5
SZELVENY_HOSSZA = 90
SORSOLASOK_SZAMA = 1

osszes = []
for szam in range(SZELVENY_HOSSZA):
    osszes.append(szam + 1)

print('lottósorsolás')
print('írd be a tippjeidet')
print(f'{TIPPEK_SZAMA} számot kell eltalálnod')
print(f'1 és {SZELVENY_HOSSZA} között kell tippelned')
print(f'{SORSOLASOK_SZAMA} sorsoláson vesz majd rész a szelvényed')

# tippek_string = input('tippjeid: ')
# tippek = []
# for s in tippek_string.split():
#     tippek.append(int(s))

hibas_tippeles = False

tippek = []
for s in input('tippjeid (szóközzel elválasztva): ').split():
    tipp = int(s)
    if tipp < 1 or tipp > SZELVENY_HOSSZA:
        hibas_tippeles = True
    tippek.append(int(s))

if len(tippek) != TIPPEK_SZAMA:
    hibas_tippeles = True

for i in range(len(tippek)):
    for j in range(len(tippek)):
        if i != j and tippek[i] == tippek[j]:
            hibas_tippeles = True

if hibas_tippeles:
    print("rosszul adtad meg a tippeket")
else:
    tippek.sort()
    print(f'tippjeid:                      {tippek}')
    for sor in range(SORSOLASOK_SZAMA):
        rnd.shuffle(osszes)
        sorsolt = []
        for i in range(TIPPEK_SZAMA):
            sorsolt.append(osszes[i])
            
        talalat = 0
        for tipp in tippek:
            if sorsolt.__contains__(tipp):
                talalat += 1

        sorsolt.sort()
        print(f'{sor}. sorsolás: kisorsolt számok: {sorsolt}')
        print(f'{sor}. sorsolás: találataid száma: {talalat}')