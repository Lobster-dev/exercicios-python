from time import sleep
Alunos = list()
Dados = list()
Dados2 = list()
Notas = list()


while True:
    Dados.append(input('Nome: ').strip().capitalize())
    Nota1 = float(input('Nota 1: '))
    Dados2.append(Nota1)
    Nota2 = float(input('Nota 2: '))
    Dados2.append(Nota2)
    Dados.append((Nota1 + Nota2)/2)
    Alunos.append(Dados[:])
    Notas.append(Dados2[:])
    Dados.clear()
    Dados2.clear()
    loop = input('Desejá continuat[S/N]: ').lower().strip()
    if loop == 'n':
        break

print('')
print(f'{"-="*14}-')
print(f'No.  {"NOME":<14} MÉDIA')


contador = 0
for Nome, Media in Alunos:
    print(f'{contador+1:<5}', end='')
    print(f'{Nome:<15}', end='')
    print(Media)
    contador += 1

print(f'{"-="*14}-')

while True:
    VisualizacaoNota = int(input('Desejá ver as notas de qual aluno (digite 0 para parar): '))
    if VisualizacaoNota == 0:
        print('FINALIZANDO...')
        sleep(2)
        print(f'{"<"*3} Volte sempre {">"*3}')
        break
    print(Notas[VisualizacaoNota-1])