n1 = int(input('quantos km será a sua viagem: '))
n2 = n1*0.45
n3 = n1*0.50
if n1>200:
    print('o valor da sua viagem é de: R${}'.format(n3))
else:
    n1<=200
    print('o valor da sua viagem é de: R${}'.format(n2))