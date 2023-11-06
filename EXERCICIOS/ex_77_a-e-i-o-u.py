palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')
for palavra in palavras:
    print(f'\nna palavra \033[1m{palavra.upper()}\033[m temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'\033[34:1m{letra.upper()}\033[m', end=' ')