from  time import  sleep
print('\033[33m','{:=^80}'.format('\033[33:4mcontagem regressiva para a queima de fogos\033[m\033[33m'))
for c in range(11, -1, -1):
    sleep(1)
    print('\033[m', c)