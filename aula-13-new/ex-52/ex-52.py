
Numero = int(input('Digite um numero para saber se ele é primo: '))
TotalDivisoes = 0

for c in range (1,Numero+1):
    if (Numero % c == 0):
        print('\033[33m', end=' ')
        TotalDivisoes = TotalDivisoes + 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end =' ')
print('')
print('O numero {} foi dividido {} vezes'.format(Numero, TotalDivisoes))
if (Numero % 1 == 0) and (Numero % Numero == 0) and (TotalDivisoes == 2):
    print('Esse número é PRIMO!!')