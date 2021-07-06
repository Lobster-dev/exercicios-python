# Sequencia de fibonacci --> 1, 1, 2, 3, 5, 8 (1 + 2 = 3 / 2 + 3 = 5 / 3 + 5 = 8) 
# a soma dos 2 números anteriores é o próximo número da sequência
 
# Numero = int(input('Digite um valor (inteiro): '))

print('= '*15)
print('   Sequencia de Fibonacci')
print('            v1.0')
print('= '*15)

QuantidadeValores = int(input('Desejá ver quantos valores da seqencia de Fibonacci (int): '))

Contador = 3

Valor1 = 0
Valor2 = 1
print(Valor1, end = ' -> ')
print(Valor2, end = ' -> ')

while Contador <= QuantidadeValores:
    Contador = Contador + 1
    Valor3 = Valor1 + Valor2  
    print(Valor3, end=' -> ')
    Valor1 = Valor2
    Valor2 = Valor3
print('Fim!!')
