PressoasMaiores = 0
Homens = 0
Mulheres = 0

while True:
    # Titulo
    print('-'*22)
    print('  Cadastre uma Pessoa')
    print('-'*22)

    # Informações
    Idade = int(input('Idade: '))
    while True:
        Sexo = input('Sexo [M/F]: ').strip().lower()
        if Sexo == 'm' or Sexo == 'f':
            break
    if Sexo == 'm':
        Homens += 1
    elif Sexo == 'f' and Idade < 20:
        Mulheres += 1
    if Idade > 18:
        PressoasMaiores += 1
    Repeticao = input('Deseja continuar [S/N]:').lower().strip()
    if Repeticao == 'n':
        break

print('-'*22)
print(f'''Pessoas com mais de 18 anos: {PressoasMaiores}
\nPessoas do sexo masculino: {Homens}\nPessoas do sexo feminino com menos de 20 anos: {Mulheres} ''')
