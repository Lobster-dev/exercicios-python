n = int(input('Digite um valor: '))

soma = 0 

while True:
    while n >= 0:
        if n / 3 == 0 or n / 5 == 0:
            soma = soma + n
            print(soma, end='->')
            n = n - 1
    if n == 0:
        break
print('acabou')