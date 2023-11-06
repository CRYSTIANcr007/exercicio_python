from random import  randint
n1 = randint(0,1000)
tentativas = 1
print('\033[1mOLÁ, SOU SEU COMPUTADOR\033[m')
print('\033[35macabei de pensar em um numero de 0 a 1000')
n2 = int(input('tente adivinhar: '))
while n1 != n2:
    if n1 > n2:
        n2 = int(input('\033[31mMAIS... tente novamente: \033[m'))
    else:
        n2 = int(input('\033[31mMENOS... tente novamente: \033[m'))
    tentativas += 1
print(f'\033[32mparabens, voce acertou o numero que eu pensei {n1}\ncom {tentativas} tentativas')