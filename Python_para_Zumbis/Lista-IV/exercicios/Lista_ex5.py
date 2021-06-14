def function_analisador_letras(msg):
    for letra in msg:
        if letra in 'python':
            return True
    return False


texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.lower()

resposta = list()

for palavra in texto.split():
    if function_analisador_letras(palavra) and len(palavra) > 4:
        resposta.append(palavra)

print(resposta)