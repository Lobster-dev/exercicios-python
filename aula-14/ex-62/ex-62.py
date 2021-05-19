# PA
# Você passa a razção e o 1° termo e ele te passa os 10 primeiros termos da PA

print("-="*13)
print("    TERMOS DE UMA PA ")
print("        PARTE 3")
print("-="*13)

PrimeiroTermo = int(input('Digite o termo inicial da sua PA: '))
Razao = int(input('Digite qual a razão dessa PA: '))
DecimoTermo = PrimeiroTermo + (10 - 1) * Razao

Contador = PrimeiroTermo
while Contador <= DecimoTermo:
    print(Contador , end = '... ')
    Contador = Contador + Razao
print('')

Repeticao = int(input("Você deseja ver mais algum termo (Digite 0 caso não deseje ver mais nenhum): "))

UltimoTermo = PrimeiroTermo + ((Repeticao+10) - 1) * Razao

while Contador <= UltimoTermo:
    print(Contador , end = '... ')
    Contador = Contador + Razao