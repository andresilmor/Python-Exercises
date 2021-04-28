#Crie um ficheiro com o nome “texto.txt”. Escreva nesse ficheiro um qualquer conteúdo
#com um número de linhas entre 20-30 (Pode ser um copy de um texto qualquer). De
#seguida, implemente e teste uma função capaz de retornar o número de vezes que
#uma dada palavra, fornecida pelo utilizador, aparece no referido texto.

def REGwordcont():
    registo=open('texto.txt','r')
    cont=0
    word=str(input('Indique a palavra pela qual procura: '))
    for line in registo:

    print('A palavra \"%s\" foi encontrada %d vezes.' %(word,cont))


REGwordcont()