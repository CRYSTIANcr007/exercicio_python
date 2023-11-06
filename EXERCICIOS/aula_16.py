lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita', )
print(sorted(lanche))#bota em ordem alfabetica
print(lanche,'\n')

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(f'variavel A {a}')
print(f'variavel B {b}')
print(f'variavel A + B = {c}')
print(f'temos {len(c)} numeros aqui dentro')# conta a quantidade de numeros que tem dentro do 'C'
print(f'quantos "2" tem dentro disso: {c.count(2)}')
print(f'a posição em que esta o "8" {c.index(8)}')
print(f'a posição em que esta o  5 {c.index(5, 1)}')

pessoa = ('crystian', 15, 73.5)
print(pessoa)
del pessoa
print(pessoa)