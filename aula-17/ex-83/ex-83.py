
expressao = input('Digite a expressão: ')
caractere = list()

for simbolo in expressao:
    if simbolo == '(':
        caractere.append('(')
    elif simbolo == ')':
        if len(caractere) > 0:
            caractere.pop()
        else:
            caractere.appen(')')
            break
if len(caractere) == 0:
    print('Sua expressão está valida')
else:
    print('Sua expressão está incorreta')