listas = []
for c in range(0, 5):
    listas.append(int(input(f'digite um valor para a posição {c}: ')))
maior = max(listas)
menor = min(listas)
print(f'o maior numero é: {maior}, e esta na posição {listas.index(maior)}')
print(f'o menor número é: {menor}, e esta na posição {listas.index(menor)}')