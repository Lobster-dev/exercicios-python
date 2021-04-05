from math import pow, sqrt
l1 = float(input('Qual o valor do cateto oposto do triangulo: '))
l2 = float(input('Qual o valor do cateto adjacente: '))
h = sqrt(pow(l1,2)+pow(l2,2))
print('A hipotenusa vai medir: {:.2f}'.format(h))