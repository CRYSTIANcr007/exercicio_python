print('\033[31m=-\033[m'*27)
print('{:=^61}'.format('\033[34mVAMOS CALCULAR OS 10 PRIMEIROS TERMOS DE UMA PA\033[m'))
print('\033[31m=-\033[m'*27)
primeio_Termo = int(input('primeiro termo: '))
razao_PA = int(input('Razão da PA: '))
termino = 0
while termino < 10:
    print(primeio_Termo, end=' → ')
    primeio_Termo += razao_PA

    termino += 1
print('fim')