n1 = int(input('digite um valor para ver a sua tabuada: '))
for c in range(1, 11):
    soma = n1 * c
    print('{} X {:2} = {}'.format(n1, c, soma))