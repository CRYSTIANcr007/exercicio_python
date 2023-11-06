n1 = int(input('digite um valor: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print(f'''\033[32m
unidade: {u}
dezena:  {d}
centena: {c}
milhar:  {m}
''')