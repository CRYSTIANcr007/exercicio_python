listagem = ('lapis', 1.76,
            'borracha', 2,
            'caderno', 15.90,
            'estojo', 25,
            'transferidor', 4.20,
            'compasso', 9.99,
            'mochila', 120.32,
            'canetas', 22.30,
            'livro', 34.90)
print('='*37)
print(f'{"listagem de preços" :^37}')
print('='*37)
for pos in range(len(listagem)):
    if pos % 2 == 0:
        print(fr'{listagem[pos]:.<30}', end='')
    else:
        print(fr'{listagem[pos]:.>7.2f}')