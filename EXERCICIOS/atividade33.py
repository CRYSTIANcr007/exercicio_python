a = int(input('primeiro valor: '))
b = int(input('segundo valor: '))
c = int(input('terceiro valor: '))
if a < b and a < c:
    menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
if a > b and a > b:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('\033[0;33mo maior número é: ', maior)
print('o menor número é: \033[m', menor)
