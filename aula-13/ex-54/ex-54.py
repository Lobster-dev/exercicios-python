from datetime import date

AnoAtual = date.today().year
MaiorIdade = 0
MenorIdade = 0

for c in range (0,7):
    AnoNasc = int(input("Em que ano a {}° pessoa nasceu: ".format(c)))
    idade = AnoAtual - AnoNasc
    if idade >= 18 :
        MaiorIdade = MaiorIdade + 1
    elif idade < 18 :
        MenorIdade = MenorIdade + 1
print('{} pessoas são maiores de idade \n {} pessoas são menores de idade'.format(MaiorIdade,MenorIdade))