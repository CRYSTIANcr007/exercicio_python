n2 = 0
n1 = 0
cont = 0
while n1 != 999:
    n1 = int(input('digite um valor: [digite 999 para sair do codigo]: '))
    n2 += n1
    cont += 1
n2 -= 999
print(f'a soma de todos os numeros é resultante a {n2}')
print(f'você digitou {cont-1} valores')