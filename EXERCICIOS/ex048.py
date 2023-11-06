soma = 0
acum = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        acum += 1
print(f'todos os {acum} numeros divisiveis por 3 e impares, somam ao total {soma}')