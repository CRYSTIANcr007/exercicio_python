from random import randint
from time import sleep
n1 = randint(0,5) # randint = sorteio
print('pensei em um numero de 0 a 5.TENTE ADIVINHAR')
print('-=-'*15)
n2 = int(input('qual o numero que eu pensei? :'))
print('-=-'*15)
if n1== n2:
    print('PROCESSANDO...')
    sleep(2)
    print('VOCÊ VENCEU O JOGO!!!   :)')
    print('o numero que eu pensei foi: ',n1)
else:
    print('você perdeu :(')
    print('o numero que eu pensei foi: ',n1)