n1 = int(input('digite um valor: '))
n2 = int(input('digite outro valor: '))
if n1>n2:
    print(f'\033[33♠mo maior número é {n1}')
elif n1 == n2:
    print('\033[33mos dois números são iguais')
else:
    print('\033[33mo maior número é {}'.format(n2))