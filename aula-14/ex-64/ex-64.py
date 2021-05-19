Repeticao = True
Soma = 0
QuantNum = 0

while Repeticao == True:
    Numero = int(input('Digite qualquer Numero (Para parar digite 999)(int): '))
    if Numero == 999:
        Repeticao = False
    else:
        Soma = Soma + Numero
        QuantNum = QuantNum + 1

print('Foram Digitados {} numeros, e a soma entre eles vale: {} '.format(QuantNum, Soma))
