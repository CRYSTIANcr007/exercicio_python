import os
cont = 0
mult = 0
while True:
    os.system("cls")
    n1 = int(input('digite um valor para calcularmos a tabuada: '))
    if n1 > 0:
        while cont < 10:
            cont += 1
            mult = n1 * cont
            print(f'{n1} X {cont:2} = {mult:2}')
    else:
        break
    cont -= 10
    input('tecle enter para prosseguir')
os.system('cls')
print('o programa foi encerrado porque o numero digitado foi um numero negativo')

