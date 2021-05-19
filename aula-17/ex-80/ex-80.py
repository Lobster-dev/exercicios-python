valores = list()

for c in range(0,5):
    n = int(input('digite um número: '))
    if c == 0 or n > valores[-1]:
        valores.append(n)
    else:
        pos = 0
        while pos < len(valores):
            if n <= valores[pos]:
                valores.insert(pos,n)
                break
            pos += 1
    

print(f'os valores digtados foram: {valores}')