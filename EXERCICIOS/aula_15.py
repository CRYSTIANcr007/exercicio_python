n = s = cont =0
while True:
    n = int(input('\033[31;1mDIGITE [00] PARA SAIR DO CODIGO\033[m digite um numero: '))
    if n == 000:
        break
    s += n
    cont += 1
print(f'o valor da soma de todos os {cont} numeros é {s}')