import datetime
hoje = datetime.date.today().year
escolha = 'S'
contFeminino = 0
cont = 0
contMasculino = 0

while True:
    sexo = ' '
    escolha = ' '
    print('_'*20)
    print('CADASTRE UMA PESSOA')
    print('_'*20)
    nome = str(input('nome: '))
    data = int(input('data de nascimento: '))
    while sexo not in 'MF':
        sexo = str(input('sexo [M/F]')).strip().upper()[0]

    idade = hoje - data

    if idade >= 18:
        cont += 1
    if sexo in 'M':
        contMasculino += 1

    if sexo in 'F':
        if idade < 20:
            contFeminino += 1
    while escolha not in 'SN':
        escolha = str(input('deseja continuar? [S/N]')).upper().strip()[0]
    if escolha not in 'S':
        break
print(f'{cont} pessoas com maior idade\n{contMasculino} homens cadastrados\n{contFeminino} mulheres com menos de 20 anos')