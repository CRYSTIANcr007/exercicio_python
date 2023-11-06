print('{:=^40}'.format('sequencia de fibonacci'))
n1 = int(input('qual a quantidade de sequencia você quer fazer: '))
cont = 0
a1 = 0
a2 = 1
while cont < n1:
    a3 = a1 + a2
    print(a3,  end=' → ')
    a1 = a2
    a2 = a3

    cont += 1
print('FIM')


