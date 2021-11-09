nevek = []

nev = 'yxz'
szamlalo = 1
while szamlalo <= 10:
    nev = input(f'írd be az {szamlalo}. nevet: ')
    if nev == '': break
    nevek.append(nev)
    szamlalo += 1

nevek.sort()
print(nevek)