# PA
# Você passa a razção e o 1° termo e ele te passa os 10 primeiros termos da PA

print("-="*13)
print("    TERMOS DE UMA PA ")
print("-="*13)

TermoInicial = int(input('Digite o termo inicial da sua PA: '))
Razao = int(input('Digite qual a razão dessa PA: '))
DecimoTermo = TermoInicial + (10 - 1) * Razao

for c in range (TermoInicial,DecimoTermo+Razao,Razao):
    print(c, end=' -> ')
print('acabou')