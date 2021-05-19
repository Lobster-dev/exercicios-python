def fatorial(n, show=False):
    """
    -> Calcula o valor de uma fatorial
    :m = numero a ser calculado
    :show = opcional, mostra ou não o valor da conta
    :return o valor da fatorial do numero n.
    """

    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ',end='')
            else:
                print(' = ', end='')
        f *= c
    return f

#fatorial(3,True)
#result = fatorial(5,True)
#print(result)
help(fatorial)