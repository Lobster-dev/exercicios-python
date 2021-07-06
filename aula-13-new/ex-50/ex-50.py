soma = 0
for c in range (0,6):
    numero = int(input('Digite o {}° valor: '.format(c)))
    print(numero % 2)
    if numero % 2 == 0:
        soma = numero + soma
print(soma)