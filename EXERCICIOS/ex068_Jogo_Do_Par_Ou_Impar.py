import random
from random import randint
cont = 0
print('\033[36m-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('-='*20)

while True:



    numMaquina = random.randint(0, 11)
    num = int(input('\033[mdigite um numero: '))
    escolha = ' '
    soma = numMaquina + num
    while escolha not in 'PpIi':
        escolha = str(input('par ou ímpar [P/I]')).strip().upper()[0]
    print(f'você jogou {num} e a maquina jogou {numMaquina}, o total de {soma}')
    if escolha == 'P':

        if soma % 2 == 0:
            print('VOCÊ VENÇEU')
            cont += 1
        else:
            print(f'GAME OVER!')
            break

    if escolha == 'I':
        if soma % 2 == 1:
            print('VOCÊ VENÇEU')
            cont += 1
        else:
            print(f'GAME OVER!')
            break
    print('vamos jogar novamente...')
print(f'você vençeu {cont} vezes')
