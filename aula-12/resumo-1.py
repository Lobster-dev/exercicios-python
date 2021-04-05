#Estruturas de controle
#Condições Alinhadas

# if ():
# elif():
# else:

nome = str(input('Qual o seu nome: ')).capitalize()
if nome == 'Roberto':
    print('Que nome bonito.')
elif nome == 'Pedro' or nome =="Maria" or nome == "Paulo":
    print('Seu nome é bem popula no Brasil')
else:
    print('olá {}'.format(nome))
print('tenha um bom dia {} :)'.format(nome))