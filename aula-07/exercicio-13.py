# você digita um valor x (nesse caso pede-se um salario ficticio) e ele lhe dara o valor com um aumento de 15%
s = float(input('Qual o salario do funcionario: R$'))
a = s+(s*0.15)
print('O funcionario ganhava R${}, mas com um aumento de 15%, ele passa a receber R%{:.2f}'.format(s,a))