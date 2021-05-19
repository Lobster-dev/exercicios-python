Repeticao = True
Numero = 0 
Soma = 0 
QuantNum = 0
MaiorValor = 0
MenorValor = 0



while Repeticao == True:
    Numero = int(input('Digite um Numero: '))
    Soma = Soma + Numero
    QuantNum = QuantNum + 1

    if QuantNum == 1:
        MaiorValor = Numero
        MenorValor = Numero
    else:
        if MaiorValor < Numero:
            MaiorValor = Numero
        elif MenorValor > Numero:
            MenorValor = Numero

    Continua = str(input('Deseja continuar[S/N]: ')).strip().lower()
    if Continua == 'n':
        Repeticao = False
    
Media = Soma / QuantNum

print('A média dos valores digitados é de: {} \nO maior valor digitado foi: {} \nO menor valor digitado foi: {}'.format(Media,MaiorValor,MenorValor))