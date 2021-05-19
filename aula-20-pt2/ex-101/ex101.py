from datetime import date 

def voto():
    nasc = int(input('Qual a sua data de nascimento: '))
    ano = date.today().year
    idade = ano - nasc
    if idade <18:
        print(f'Você tem {idade} anos \nNao precisa votar')
    elif idade <65:
        print(f'Você tem {idade} anos \nVoto obrigatorio')
    else:
        print(f'Você tem {idade} anos \nVoto facultativo')


voto()