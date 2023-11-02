'''
Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

'''
maior = 0
menor = 0
print('\033[31m\nUM NUMERO TEM POR OBRIGAÇÃO SER MAIOR QUE O OUTRO\n PARA O PROGRAMA RODAR DO JEITO QUE É PRA SER\033[m')
n1 = 0
n2 = 0
while n1 == n2:
    n1 = int(input('digite um valor: '))
    n2 = int(input('digite outro valor: '))
    if n1 != n2:
        maior = max(n1, n2)
        menor = min(n1, n2)
        while maior > menor:
            print(f'\033[m{menor}\033[36m', end=' - ')
            menor += 1
        print(f'\033[m{maior}')
    else:
        print('\033[31mo valor deve ser maior que o outro, por favor tente novamente\033[m')