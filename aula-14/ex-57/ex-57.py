# Validação de Dados
repeticao = False
while repeticao == False:
    Sexo = input('Digite o seu sexo [M/F] : ').lower()
    if Sexo == 'm' or Sexo == 'f':
        repeticao = True
    else: 
        print('Digite novamente')
        repeticao = False
print('final')
