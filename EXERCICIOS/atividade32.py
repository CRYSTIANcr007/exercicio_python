from datetime import  date
n1 =int(input('qual ano quer analizar. sendo 0 o nosso ano atual'))
if n1==0:
    n1 = date.today().year
    if n1 %4 ==0 and n1%100 !=0 or n1%400 ==0:
    print('sim, esse ano é bissexto')
else:
    print('nao, esse ano não é bissexto')