'''
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor
seja inválido e continue pedindo até que o usuário informe um valor válido

'''

n1 = float(input('digite a nota do aluno: '))
while n1 < 0 or n1 > 10:
    print('\033[31mVALOR DIGITADO INVÁLIDO')
    n1 = float(input('\033[mdigite novamente: '))
print(f'a nota do aluno é {n1}')
