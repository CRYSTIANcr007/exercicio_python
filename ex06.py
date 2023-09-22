'''O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de R$1,99 e agora
possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora
rudimentar. O programa deverá receber um número desconhecido de valores referentes aos
preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final da
compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o
cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação, o programa
deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve ser conforme o

exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
'''

preco = ''
total = 0
cont = 1
print('DIGITE 0 PARA PAGAR OS PRODUTOS')
while preco != 0:
    preco = float(input(f'produto {cont}: R$'))
    total += preco
    cont += 1

dinheiro = float(input('quanto você vai pagar: R$'))
troco = dinheiro - total
if troco < 0:
    print('\033[31mvamos cancelar a compra, pois o valor pago nao foi o suficiente')
elif troco == 0:
    print('volte sempre')
else:
    print(f'compra realizada com sucesso\n\033[32mo troco é de R${troco}')