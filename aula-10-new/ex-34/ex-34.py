salario = float(input('Qual o valor do funcionario: '))
if salario <= 1250:
    juros = (salario*0.15)+salario
    print('Quem ganhava {} passa a ganhar {}'.format(salario, juros))
else:
    juros = (salario*0.10)+salario
    print('Quem ganhava {} passa a ganhar {}'.format(salario, juros))
