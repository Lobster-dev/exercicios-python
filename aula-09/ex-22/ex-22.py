nome = str(input('Digite o seu nome: ')).strip()
print('Analisando o seu nome...')

print('Seu nome em Maiusculo: {}'.format(nome.upper()))
print('Seu nome em minusculo {}'.format(nome.lower()))
print('Seu nome tem ao todo: {} letras'.format(len(nome)-nome.count(' ')))
# print ('Seu 1° nome tem: {} letras'.format(nome.find(' ')))
NomeSeparado = nome.split()
print("Seu 1° nome tem ao todo: {} Letras".format(len(NomeSeparado[0])))