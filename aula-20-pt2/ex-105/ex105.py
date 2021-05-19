from time import sleep

def notas(sit=False):
    """-> Função para analisar várias notas de um aluno 
    :nota uma ou mais notas
    :sit opcional mostra a situação do aluno
    :return dicionario com várias notas do aluno"""

    values = dict()
    media = QuantidadeTotalDeNotas = contador = maior = menor = 0

    #validador de numero
    while True:
        number = str(input('Digite a nota do aluno: ')).strip()
        if number.isnumeric():

            #conversor de str pra valor inteiro
            number = int(number)

            #meda, total de numeros e contador pra 
            media += number
            QuantidadeTotalDeNotas += 1
            contador += 1

            #maior e menor
            if contador == 0:
                maior = number
                menor = number
            else:
                if number > maior:
                    maior = number
                if number < menor:
                    menor = number

            loop = input('Desejá inserir outra onta para o aluno [S/N]: ').lower().strip()
            
            if loop == 'n':
                break
        else:
            print('VALOR INCORRETO!!')

    media = media / QuantidadeTotalDeNotas

    values['Total'] = QuantidadeTotalDeNotas
    values['Maior'] = maior
    values['Menor'] = menor
    values['Media'] = media

    if sit:
        if media >= 70:
            values['Sit'] = 'Boa'
        elif media >= 50:
            values['Sit'] = 'Necessita de melhoria'
        else: 
            values['Sit'] = 'Ruim'
        sleep(0.5)
        print(values)
    else:
        sleep(0.5)
        print(values)


def GeraLinha(msg):
    print(f'{"="*20}')
    print(f'{msg:^22}'.upper())
    print(f'{"="*20}')
    #



#total(quantidade de notas colocadas), maior(maior nota colocada), menor(nota colocada), média(de todas as notas), 
#situação(valor opcional, mostra a situação do aluno)

GeraLinha('Calculo notas')

while True:
    print('Digite a opção necessária')
    print('[ 1 ] Com situação\n[ 2 ] Sem situação')

    option = str(input('')).strip()
    if option == '1':
        notas(sit=True)
    else:
        notas()

    print('')
    print('Pressione qualquer tecla para continuar')
    refaz = str(input('Desejá refazer o processo [S/N]: ')).lower().strip()
    if refaz == 'n':
        break