def escrever(msg):
    tamanho = len(msg) + 2
    print(f'-'*tamanho)
    print(f' {msg}')
    print(f'-'*tamanho)


texto = input("Digite uma frase: ")
escrever(texto)

