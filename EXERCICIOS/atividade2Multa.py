n1 = int(input('velocidade do carro: '))
n2 = (n1-80)*7
if n1> 80:
    print('você foi multado por escesso de volocidade.\no valor da multa é de R${},00'.format(n2))
else:
    n1<80
    print('tudo certo, você não foi multado')