n = int(input('digite um valor: '))
c = n
fat = 1
while c >= 1:
    fat *= c
    print(c, 'x ' if c > 1 else '= ', end='')
    c -= 1
print(fat)