sexo = str(input('informe seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'sexo {sexo} registrado com sucesso')