peso = float(input('qual seu peso? (kg): '))
altura = float(input('qual sua altura? (m): '))
mic = peso / altura ** 2
print('seu IMC é {:.1f}, '.format(mic), end='')
if mic < 18.5:
    print('você está abaixo  do peso')
elif mic >= 18.5 and mic < 25:
    print('você esta no peso ideal')
elif mic >= 25 and mic < 30:
    print('você está no sobrepeso')
elif mic >= 30 and mic <40:
    print('você esta obeso(a)')
elif mic > 40:
    print('você está na obesidade mórbida')
