import random
print('escolha um aluno para apagar a louça')
print('-='*18)
n1 = input('\033[31mprimeiro aluno: ')
n2 = input('\033[31msegundo aluno: ')
n3 = input('\033[31mterceiro aluno: ')
n4 = input('\033[31mquarto aluno: ')
n5 = input('\033[31mquinto aluno: ')
lista = [n1, n2, n3, n4, n5]
escolhido = random.choice(lista)
print(f'\033[34mo aluno escolhido foi: {escolhido}')