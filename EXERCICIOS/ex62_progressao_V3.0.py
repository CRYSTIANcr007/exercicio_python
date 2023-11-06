print('gerador de PA')
print('=-'*10)
primeiro = int(input('primeiro termo: '))
razao = int(input('razão da PA: '))
termo = primeiro
cont = 0
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('\033[7m{} → '.format(termo), end='')
        termo += razao
        cont += 1
    print('pausa\033[m ')
    mais = int(input('\033[m quantos termos você quer mostrar a mais?'))
print('\033[1;31mfinalizamos o programa com {} termos imprimidos na tela '.format(cont-1))