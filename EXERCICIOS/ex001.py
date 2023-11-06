valordacasa = float(input('VALOR DA CASA: R$'))
#perguntar o salario dele
salario = float(input('SEU SALARIO: R$'))
#perguntar em quantos anos ele vai pagar a casa
quantosanosdepagamento = int(input('QUANTOS ANOS VOCÊ VAI PAGAR A CASA? '))

#pegar a quantidades de meses para dividir as parcelas
meses = quantosanosdepagamento*12
#valor das mensalidades
mensalidade = float(valordacasa / meses)
#calcular os 30% do salario dele para ver se as mensalidades serao compativeis com o combinado
trinta = (salario*30)/100
#se a mensalidade corresponder a 30% ou menos que seu salario. salario aprovado
if trinta > mensalidade:
    print('SEU EMPRESTIMO FOI APROVADO :)')
    print('a sua mensalidade sera de R${:.2f}'.format(mensalidade))
#se nao, emprestimo negado
else:
    print('EMPRESTIMO NEGADO :(')