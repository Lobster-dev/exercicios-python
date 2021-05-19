# Fatorial
numero = int(input('Digite um número para saber sua fatorial: '))
contador = numero
fatorial = numero
while 1 < contador <= numero:
    fatorial = fatorial * (contador-1)
    contador = contador - 1

print(fatorial)