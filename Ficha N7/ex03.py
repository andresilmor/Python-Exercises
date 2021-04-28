#Tendo por base o ficheiro da questão 1, implemente um programa capaz de pesquisar
#e mostrar os nomes completos existentes que obedeçam ao critério de pesquisa
#“nome próprio”. Assim, o utilizador deverá introduzir um dado nome próprio para
#pesquisa e, o output, deverá ser o conjunto de nomes completos onde o nome próprio
#a pesquisar está presente.

def REGnome():
    registo=open('pessoas.txt','a')
    text=-1
    while text!='':
        text=str(input('Insira um nome:\n'))
        registo.write(text+'\n')
    registo.close()

def REGsearch():
    registo=open('pessoas.txt','r')
    print('-'*80)
    pesq=str(input('Indique o nome pelo qual quer procurar:\n'))
    cont=0
    for line in registo:
        if pesq in line:
            print(line,end='')
            cont+=1
    if cont==0:
        print('Não foi encontrado nenhum nome.')
    registo.close()

REGnome()
REGsearch()
