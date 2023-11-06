from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    data = int(input(f'\033[36mano de na nascimento da {c}ª pessoa: '))
    if atual - data > 21:
        maior += 1
    else:
        menor += 1
print(f'\033[35:1mquantidade de pessoas que atingiram a maior idade: {maior}\nquantidade de pessoas que ainda nao atingiram a maior idade: {menor}')