import random

# lista = []
# for i in range(6):
#     lista.append(random.randint(0, 9))
# for x in lista:
#     print(x)
# print('-------------------')
# print(lista[4])

nevek = []
magassagok = []

db = 3

for i in range(db):
    nevek.append(input(f'add meg az {i}. nevet: '))
    magassagok.append(int(input(f'add meg {nevek[i]} magasságát: ')))

# átlagmagasság:
sum = 0
for m in magassagok:
    sum += m
print(f'átlagmagasság: {sum / db}')