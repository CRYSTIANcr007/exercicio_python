from random import randint
tuplas = randint(0, 10) ,randint(0, 10) ,randint(1, 10) ,randint(1, 10) ,randint(1, 10)
for c in tuplas:
    print(c, end=' - ')
print(f'\no maior valor sorteado foi {max(tuplas)}')
print(f'o menor valor sorteado foi {min(tuplas)}')
