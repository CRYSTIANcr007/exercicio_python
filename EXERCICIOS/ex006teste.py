idade = int(input('sua idade: '))
if idade <= 9:
    print('você está na classificação MIRIM')
elif idade > 9 and idade <= 14:
    print('você está na categoria INFANTIL')
elif idade > 14 and idade <= 19:
    print('você está na catergoria JÚNIOR')
elif idade > 19 and idade <= 25:
    print('você está na categoria SÊNIOR')
elif idade > 25:
    print('você está na categoria MASTER')
