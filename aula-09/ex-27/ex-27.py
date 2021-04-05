nome = str(input('Digite o seu nome completo: ')).lower().strip().split()
print('Se primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é: {}'.format(nome[len(nome)-1]))
