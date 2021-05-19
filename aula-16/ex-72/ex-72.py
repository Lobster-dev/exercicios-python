NumerosExtenso = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis','sete','oito', 'nove' ,'dez' ,'onze' ,'doze' ,'treze' ,'quatorze' ,'quinze' ,'deseseis' ,'desesete' ,'desoito' ,'desenove' ,'vinte')

while True: 
    numero = int(input('Digite um numero entre 0 e 20: '))
    if numero > 20 or numero < 0:
        print('tente novamente!', end =' ')
    else:
        break
print(f'Você digitou o numero: {NumerosExtenso[numero]}')