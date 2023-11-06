print('-'*40)
print('{:=^40}'.format('OS 10 TERMOS DE UMA PA'))
print('-'*40)
n1 = int(input('primeiro termo: '))
n2 = int(input('razão: '))
n3 = n1 + (10 - 1) * n2
for c in range(n1, n3 + n2, n2):
    print(c,end=' → ')
print('ACABOU')