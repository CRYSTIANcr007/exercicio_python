cont = media = soma = 0
while True:
    n1 = int(input('digite um valor: '))
    if n1 == 999:
        break
    soma += n1
    cont += 1
media = soma/cont

print(f'você digitou {cont} numeros\na soma de todos eles foi {soma}\na media de todos eles é {media:.0f}')