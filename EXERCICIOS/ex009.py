print('{:=^40}'.format('\033[34mCASAS BAHIA\033[m'))
preco = float(input('\033[mqual o valor da compra? R$'))
print('''         \033[4MFORMAS DE PAGAMENTO
 \033[31m[1] à vista dinheiro/cheque\033[m
 \033[32m[2] à vista cartão\033[m
 \033[33m[3] 2x no cartão\033[m
 \033[34m[4] 3x ou mais no cartão\033[m
''')
opcao = int(input('\033[7:1:40mqual sera a sua opção?\033[m '))
if opcao == 1:
    desconto = preco/10
    precofinal = preco - desconto
    print('\033[31mvocê ganhou um desconto de 10%. o valor que você vai pagar será R${:.2f}'.format(precofinal))
elif opcao == 2:
    desconto = (preco * 5) / 100
    precofinal = preco - desconto
    print('\033[32mvocê ganhou um deconto de 5%. o valor final da sua compra será: R${:.2f}'.format(precofinal))
elif opcao == 3:
    precofinal = preco / 2
    print('\033[33mvocê dividiu em 2x. você pagará 2 parcelas de R${:.2f}'.format(precofinal))
elif opcao == 4:
    parcelas = int(input('\033[34mquantas vezes você quer parcelar? '))
    juros = (preco * 20)/100
    precofinal = preco + juros
    mensalidade = precofinal / parcelas
    print('você recebeu juros de 20%. sua mensalidade será de {:.2f}\n\033[4mTOTAL DA COMPRA {:.2f}'.format(mensalidade, precofinal))
else:
    print('tu é burro ou cego? as unicas opções q tem é 1, 2, 3 e 4. E tu marcou {}'.format(opcao))
