from datetime import datetime

Dados = dict()
Ano = datetime.now().year


Dados['Nome'] = input('Nome: ').strip().capitalize()
AnoNasc = int(input('Ano de nascimento: '))
Dados['Idade'] = Ano - AnoNasc
Dados['CarteiraTrabalho'] = int(input('Carteira de trabalho (0 nao tem): '))
if Dados['CarteiraTrabalho'] != 0:
    Dados['AnoContratacao'] = int(input('Ano de contratação: '))
    Dados['Salario'] = int(input('Salario: R$'))
    TempoContribuicao = Ano - Dados['AnoContratacao']
    Aposentadoria = 33 - TempoContribuicao
    Dados['Aposentadoria'] = Dados['Idade'] + Aposentadoria


print('')
print(f'{"-="*20}-')
print('')

print(Dados)
for Key, Value in Dados.items():
    print(f'{Key} -> {Value}')