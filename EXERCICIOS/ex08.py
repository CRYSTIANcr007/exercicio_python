#       Faça um programa que leia e valide as seguintes informações:
#       Nome: maior que 3 caracteres;
#       Idade: entre 0 e 150;
#       Salário: maior que zero;
#       Sexo: ’f’ ou ’m’;
#       Estado Civil: ’s’, ’c’, ’v’, ’d’;



#NOME
nome = input('nome: ').strip().upper()
quantidadeLetras = len(nome)
while quantidadeLetras < 3:
    print('a quantidade de caracteres tem que ser maior que 3')
    nome = input('digite novamente: ')
    quantidadeLetras = len(nome)


#IDADE
idade = int(input('digite a idade: '))
while idade <= 0 or idade >= 150:
    print('A IDADE TEM QUE SER MAIOR QUE 0 E MENOR QUE 150')
    idade = int(input('digite novamente: '))
#SALARIO


salario = float(input('salario: '))
while salario <= 0:
    print('o salario tem que ser maior que 0')
    salario = float(input('digite novamente: '))


# SEXO

sexo = (input('sexo [M/F]: ')).upper()
while sexo not in 'MF':
    sexo = input('digite novamente o sexo [M/F]: ').upper()

# ESTADO CIVIL

estado_Civil = input('estado civil [S / C / V / D]: ').upper()
while estado_Civil not in 'SCVD':
    print('os valores tem que ser S/ C/ V / D')
    estado_Civil = input('estado civil [S / C / V / D]: ').upper()