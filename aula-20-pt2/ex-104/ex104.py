def leiaint(msg):
    while True:
        number = str(input(msg)).strip()
        if number.isnumeric():
            break 
        else:
            print('VALOR INCORRETO!!')
    print(f'Você digitou o número: {number}')


leiaint('digite um numero: ')