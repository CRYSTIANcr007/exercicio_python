tupla = (int(input('digite um valor :')),
         int(input('digite um valor :')),
         int(input('digite um valor :')),
         int(input('digite um valor :')), )
print(f'o valor 9, apareceu {tupla.count(9)}')
if 3 in tupla:
    print(f'o valor 3 apareceu na posição {tupla.index(3)+1}')
else:
    print('o valor 3 não foi digitado em nenhuma posição')
print('os valores pares foram: ', end=' ')
for c in tupla:
    if c % 2 == 0:
        print(c, end= ' ')