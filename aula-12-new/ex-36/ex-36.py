ValorCasa = float(input('Qual o valor da casa: '))
SalarioComprador = float(input('Qual o salario do comprador: '))
FinanciamentoAnos = float(input('Deseja financiar em quantos anos: '))

print('')

AnosTotal = FinanciamentoAnos * 12
SalarioTotal = SalarioComprador * AnosTotal
ValorCasaTotal = ValorCasa / AnosTotal
# O valor de cada prestação não pode exeder 30% do salario mensal do jovem.
SalarioTotalMes = SalarioComprador * 0.3

if SalarioTotalMes >= ValorCasaTotal:
    print('Financiamento Aprovado!!')
    print('O valor da prestação será de R${:.2f} mês'.format(ValorCasaTotal))
elif SalarioTotalMes < ValorCasaTotal:
    print('Financeamento negado!!')
    print('O valor da parcela que é de R${:.2f} mês exede a regra de 30% do seu salário'.format(ValorCasaTotal))
