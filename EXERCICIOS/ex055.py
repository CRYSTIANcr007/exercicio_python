menor = 0
maior = 0
for c in range(1, 6):
    peso = float(input(f'peso da {c}ª pessoa: '))
    if c == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('a pessoa com o maior peso esta pesando Kg{:.2f}\na pessoa com o menor peso esta pesando Kg{:.2f}'.format(maior, menor))
