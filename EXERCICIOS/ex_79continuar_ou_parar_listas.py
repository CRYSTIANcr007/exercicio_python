listas = []
escolha = 'S'
while True:
    listas.append(int(input('digite um valor: ')))
    while escolha not in 'Ss':
        escolha = input('deseja continuar? [S/N]: '.upper())
print(listas)