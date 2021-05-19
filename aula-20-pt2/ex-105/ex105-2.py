def notas():
    """-> Função para analisar várias notas de um aluno 
    :nota uma ou mais notas
    :sit opcional mostra a situação do aluno
    :return dicionario com várias notas do aluno"""
    
    values = dict()

    #validador de numero
    while True:
        number = str(input('Digite a nota do aluno: ')).strip()
        if number.isnumeric():
             loop = input('Desejá inserir outra onta para o aluno [S/N]: ').lower().strip()
             if loop == 'n':
                 break
        else:
            print('VALOR INCORRETO!!')
    number = int(number)

notas()