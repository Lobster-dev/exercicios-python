# Vocẽ digita uma palavra qualquer e ele te diz todas as informaçãoes possiveis sobre ela 
p = input('Digite algo: ')
print('O tipo primitivo desse valor é: ', type(p))
print('Só tem espaços: ', p.isspace())
print('É um numero', p.isnumeric())
print('É alfabetico: ', p.isalpha())
print('É alfanumérico: ', p.isalnum())
print('Está em maiusculas: ', p.isupper())
print('Está em minusculas: ', p.islower())
print('Está captalizado: ', p.istitle())05