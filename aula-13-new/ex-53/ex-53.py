
Frase = input('Digite um frase: ').strip().lower().replace(" ", "")

Inverso = ''
for c in range (len(Frase)-1,-1,-1):
    Inverso = Inverso + Frase[c]
print('O inverso de {} é {}'.format(Frase, Inverso))
if Frase == Inverso:
    print('Essa frase é um PALÍNDROMO!!')
else:
    print('Essa frase não é um PALÍNDROMO')