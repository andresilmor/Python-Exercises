#Tendo por base o ficheiro da questão 1, coloque num objeto do tipo List, todos os
#nomes existentes no ficheiro. De seguida mostre o conteúdo do tipo List que definiu
#de forma a verificar que tudo correu bem.
#AVISO: Para guardar nomes no ficheiro usar def do ex1/2/3

def REGlistar():
    listagem=[]
    registo=open('pessoas.txt','r')
    for line in registo:
        listagem.append(line[:-1])
    print('Lista de nomes: ')
    print(listagem)

REGlistar()