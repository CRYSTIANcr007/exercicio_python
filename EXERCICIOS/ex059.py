n1 = int(input('PRIMEIRO NUMERO: '))
n2 = int(input('SEGUNDO NUMERO: '))
n3 = 0
while n3 != 5:
    n3 = int(input('''\033[1m
    opcoes:
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros 
    [5] sair do programa
    QUAL SUA OPCAO: \033[m'''))
    # SOMA
    if n3 == 1:
        soma = n1 + n2
        print(f'\033[31mo valor da soma é: {soma}\033[m')

    # multiplicação
    elif n3 == 2:
        mult = n1 * n2
        print(f'\033[31mo valor da multiplicação é : \033[m{mult}')

    # MAIOR NUMERO DOS DOIS
    elif n3 == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'\033[32mo maior dos dois numeros é: \033[m{maior}')

    # NOVOS NUMEROS
    elif n3 == 4:
        n2 = int(input('\033[35mnovo numero: \033[m'))
        n1 = int(input('\033[35mnovo numero: \033[m'))

