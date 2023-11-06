s = 0
for c in range(1, 7):
    n1 = int(input('digite um valor: '))
    if n1 % 2 == 0:
        s += n1
print('a soma dos valores pares são {}'.format(s))