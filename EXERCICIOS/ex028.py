from time import sleep
from random import randint
from time import sleep
n1 = randint(0,5)          #vai sortear um número de 0 a 5
n2 = int(input('digite um número: '))
print('CARREGANDO...')
sleep(2)
if n1 == n2:
    print(f'''o numero em que eu pensei foi:{n1}. VOCÊ ME VENÇEU 
:(''')
else:
    print(f'o numero que eu pensei foi: {n1}.VOCÊ PERDEU HAHAHAHA :)')