def formatacao(msg):
    print(f"{'-='*10}-")
    print(f'{msg:^21}')
    print(f"{'-='*10}-")

def terreno():
    largura = float(input('Largura(m): '))
    comprimento = float(input('Comprimento(m): '))
    area = largura * comprimento
    print(f'A area de um terreno com {largura:.1f} x {comprimento:.1f} é de {area:.2f}m²')


formatacao('CONTROLE DE TERRENO')
terreno()