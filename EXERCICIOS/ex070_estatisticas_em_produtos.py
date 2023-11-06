maisBarato = 99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999
totalGasto = cont = conta =  0
maisBaratoProduto = ' '
while True:
    escolha = ' '

    nomeProduto = str(input('nome do produto: '))
    precoProduto = float(input('preço do produto: R$'))
    while escolha not in 'SN':
        escolha = str(input('quer continuar [S/N]')).upper().strip()[0]
    if precoProduto < maisBarato:
        maisBarato = precoProduto
        maisBaratoProduto = nomeProduto


    if precoProduto >= 1000:
        cont += 1
    totalGasto += precoProduto
    if escolha != 'S':
        break

print('{:=^40}'.format('FIM DO PROGRAMA'))
print(f'o total gasto foi R${totalGasto:2}')
print(f'temos {cont} produtos com o valor acima de R$1000')
print(f'o produto mais barato é {maisBaratoProduto}, custando {maisBarato}')