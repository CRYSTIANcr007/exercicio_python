'''
Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa
anual de crescimento de 3% e que a população de B seja 200000 habitantes com uma taxa de
crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários
para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento

'''

pop_a = 80000
pop_b = 200000
cont = 0

taxa_crescimento_a = 0.03
taxa_crescimento_b = 0.015
while pop_a < pop_b:
    pop_a += taxa_crescimento_a * pop_a
    pop_b += taxa_crescimento_b * pop_b
    cont += 1
print(f'a população A vai demorar {cont} anos para alcançar a população B')

