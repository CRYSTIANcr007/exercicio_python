cont = 0
media = 0
resposta = 'S'
maior = 0
menor = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
while resposta in 'Ss':
    n1 = int(input('digite um número: '))
    media += n1
    resposta = input('deseja continuar? [s/n]: ').strip().upper()
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1


    cont += 1
media /= cont
print(f'você digitou {cont} números e a média foi {media}\nO maior valor foi {maior}, e o menor foi {menor}')