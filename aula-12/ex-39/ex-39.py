from datetime import date

AnoAtual = date.today().year

AnoNascimento = int(input('Ano de nascimento: '))

if AnoNascimento > AnoAtual:
        print('ANO INVALIDO!!')
        print('Tente novamente')

idade = AnoAtual - AnoNascimento

if idade >= 18:
    JaSeAlistou = str(input('Já se alistou [S/N] : ')).lower().strip()

if idade == 18 and JaSeAlistou == 'n':
    print('Você deve se alistar esse ano')
elif idade > 18 and JaSeAlistou == 'n':
    AnoAlistamento = idade - 18
    print('Você já deveria ter se alistado')
    print('Já se passaram {} anos do seu periodo de alistamento'.format(AnoAlistamento))
elif idade < 18:
    AnoAlistamento = 18 - idade
    print('Falatam {} anos para você se alistar'.format(AnoAlistamento))
elif idade >= 18 and JaSeAlistou ==  's':
    print('Então está tudo em ordem')
