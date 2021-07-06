# o comando " break " interrompe um laço de repetição
# " while True " laço de repetição infinita 

n = s = 0

while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
# Modo normal
# print('A soma valer {}'.format(s))

# Modo f string 
print(f'A soma vale {s}') #python 3.6 pu maior