n1 = int(input('digite um número: '))
print('''para qual você quer converter
[ 1 ] BINÁRIO
[ 2 ] HEXADECIMAL
[ 3 ] OCTAL
''')
n2 = int(input('digite para escolher: '))
if n2 == 1:
    print(f'conversão para BINÁRIO: {bin(n1)}')
elif n2 == 2:
    print(f'conversão para HEXADECIMAL: {hex(n1)}')
elif n2 == 3:
    print(f'conversão para OCTAL: {oct(n1)}')
else:
    print('tu é retardado??? 1, 2 ou 3. E não {} imbecil'.format(n2))