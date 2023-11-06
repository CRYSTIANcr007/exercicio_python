maioridadehomem = 0
nomevelho = ''
mediaidade = 0
mulhermenor = 0

for c in range(1, 5):
    print(f'\033[1;35m_____{c}ª PESSOA _____\033[m')
    nome = str(input('\033[1mNOME: ')).strip()
    idade = int(input('IDADE: '))
    sexo = str(input('sexo [M/F]: \033[m')).strip()
    mediaidade += idade

    if c == 1 and sexo in 'Mm':
        maioridadehomem += idade
        nomevelho += nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        mulhermenor += 1

print('\033[34mo homem mais velhor tem {} anos, e o seu nome é {}'.format(maioridadehomem, nomevelho))
print('\033[34ma media de idade do grupo é de: {}'.format(mediaidade / 4))
print(f'\033[34mao todo, temos: {mulhermenor} mulheres com menos de 20 anos.')