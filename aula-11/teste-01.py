# Para utilizar cores no terminal você utiliza o comando " \033[      m "
# dentro desse codigo serṕa colocado o style(estilo);text(texto);back(fundo);
# codigos de estilo => 0(sem nada),1(negrito),4(sublinhado),7(Inverte as configurações funndo <--> letra) 
# Codigos de texto => 30 --> 37 que demoniman as cores( branco(30), vermelho(31), verde(32), amarelo(33), azul(34), roxo(35), ciano(36), cinza(37))(para colocar mais usear uma biblioteca)
# back cores de fundo => 40 --> 47 (mesmas cores do texto)

# fundo vermelho letra branca \033[0;30;41m
# ==> \033[0;30;41m
#Fundo azul letra amarela e sublinhada \033;[4;33;44m
# ==> \033;[4;33;44m
#Fundo amarelo letra em roxo com negrito \033[1;35;43m
# ==> \033[1;35;43m
#Letra cinza fundo preto \033;[30;42m
# ==> \033;[30;42m
# fundo preto letra cinza \[033m (desfaz as configurações)
# ==> \[033m
#fundo branco letra preta \033[7;30m (ele inverte as configurações de fundo com as de letra)
# ==> \033[7;30m
