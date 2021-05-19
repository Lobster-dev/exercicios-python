def ficha(nome,gols):
    """-> recebe o nome e a quantidade de gols de um jogador,
    :caso algum dos dados do jogador não sejam informados ele 
    :os colocara como desconhecido(para texto) e 0(para numerico)"""
    print(f'O jogador {nome} marcou {gols} gols na partida')

def linha(msg):
    print(f'{"-="*10}-')
    print(f' {msg} ')
    print(f'{"-="*10}-')

linha('Ficha de cadastro')
name = str(input('Digite o nome do jogador: '))
gols = str(input('Digite a quantidade de gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if name.strip() == '':
    ficha('<desconhecido>',gols)
else:
    ficha(name,gols)

ajuda = input('deseja ver a descrição de ficha? ').lower().strip()
if ajuda == "s":
    help(ficha)