n1 = float(input('\033[34mprimeiro seguimento: '))
n2 = float(input('segundo seguimento: '))
n3 = float(input('terceiro seguimento: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1:
    print('\033[35mpodemos formar um trângulo sim', end='')
    if n1 == n2 == n3:
        print('\033[35m, e esse triângulo é \033[4mEQUILÁTERO')
    elif n1 != n2 != n3 != n1:
        print('\033[35m, e esse triângulo é \033[4mESCALENO')
    elif n1 == n2 or n1 == n3 or n2 == n3:
        print('\033[35m, e esse triângulo é \033[4mISÓSCELES')
else:
    print('não podemos formar triângulo ')