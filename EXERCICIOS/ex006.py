from datetime import date
ano = int(input('ano em que você nasceu: '))
atual = date.today().year
idade = atual - ano
print(f'sua idade é {idade}')
if idade <= 9:
    print('sua categoria: MIRIM')
elif idade > 9 and idade <= 14:
    print('sua categoria: INFANTIL')
elif idade > 14 and idade <= 19:
    print('sua categoria: JUNIOR')
elif idade > 19 and idade <= 25:
    print('sua categoria: SÊNIOR')
else:
    print('sua categoria: MASTER')