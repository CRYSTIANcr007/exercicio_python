import random

n1 = input('um nome:')
n2 = input('outro nome: ')
n3 = input('outro nome: ')
n4 = input('outro nome: ')
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print(lista)