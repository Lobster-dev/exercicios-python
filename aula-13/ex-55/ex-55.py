
MaiorPeso = 0
MenorPeso = 0

for Pessoa in range (5):
    Peso = float(input("Peso da {}° pessoa: ".format(Pessoa+1)))

    if Pessoa == 0: 
        MenorPeso = Peso
        MaiorPeso = Peso
    else: 
        if Peso < MenorPeso:
            MenorPeso = Peso
        if Peso > MaiorPeso:
            MaiorPeso = Peso

print("menor {}, maior {}".format(MenorPeso, MaiorPeso))