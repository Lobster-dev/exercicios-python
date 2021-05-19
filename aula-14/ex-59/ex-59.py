# Menu de opções
looping = True
while looping == True:
    Numero1 = float(input('Digite um valor: '))
    Numero2 = float(input('Digite outro valor: '))

    print('')

    print('Oque você deseja fazer com esses números')
    operacoes = ['somar','multiplicar','maior','novos números','sair do programa']

    looping2 = True
    while looping2 == True: 
        for c in range (5):
            print('[ {} ] {}'.format(c+1, operacoes[c]))

        resposta = int(input('Qual operação deseja fazer: '))
        print('')

        if resposta == 1:
            print('{} + {} = {}'.format(Numero1,Numero2,Numero1+Numero2))
            print('')
        elif resposta == 2: 
            print('{} x {} = {}'.format(Numero1,Numero2,Numero1*Numero2))
            print('')
        elif resposta == 3: 
            if Numero1 > Numero2: 
                print('{} > {} '.format(Numero1,Numero2))
                print('')
            elif Numero1 < Numero2:
                print('{} < {}'.format(Numero1,Numero2))
                print('')
            elif Numero1 == Numero2:
                print('{} = {}'.format(Numero1,Numero2))
                print('')
        elif resposta == 4: 
            looping = True
            looping2 = False
        elif resposta == 5: 
            looping = False
            looping2 = False