print('\033[36mVAMOS FORMAR UM TRIÂNGULO')
print(30 * '-=-=')
a = float(input('\033[m\033[33mseguimento A: '))
b = float(input('seguimento B: '))
c = float(input('seguimento c: \033[m'))
if a + b > c:
    print('\033[4mSIM É POSSIVEL fazer um triângulo com os seguimentos acima')
else:
    a + b < c
    print('\033[4mNÃO É POSSIVEL fazer um triângulo com os seguimentos acima')