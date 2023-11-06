lanche = ('hamburguer', 'suco', 'pizza', 'pudim', 'batata frita')
for cont in range(0, len(lanche)):
    print(f'vou comer {lanche[cont]} posição {cont}') #mostra a posição da comida e o nome da comida
print('puxa!!! comi pra caramba \n')


for pos, comida in enumerate(lanche) :
   print(f'eu vou comer {comida} posição {pos}')
print('puxa!!! comi pra caramba\n')

for comida in lanche:
    print(comida)