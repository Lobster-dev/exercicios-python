texto = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you.'''.replace(',','').replace('.','').lower().split()

resposta = list()

for palavra in texto:
    if palavra[0] in 'python' or palavra[-1] in 'python':
        resposta.append(palavra)

print(resposta)