valor = int(input('Digite um valor: '))
print('''escolha umas das bases de conversão
[ 1 ] converter para BINARIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')
resposta = int(input(''))
Binario = bin(valor)[2:]
Octal = oct(valor)[2:]
Hexadecinal = hex(valor)[2:]
if resposta == 1:
    print('{} convertido para BINARIO é: {}'.format(valor, Binario))
elif resposta == 2:
    print('{} convertido para OCTAL é: {}'.format(valor, Octal))
elif resposta == 3:
    print('{} convertido para HEXADECIMAL é: {}'.format(valor, Hexadecinal))