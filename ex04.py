'''
Faça um programa que leia 5 números e informe a soma e a média dos números.

'''
n1 = 0
media = 0
for c in range(1, 6):
    n1 = int(input('digite um valor: '))
    media += n1
print(f'a soma entre eles é {media}\na media dos numeros é de: {media / 5}')