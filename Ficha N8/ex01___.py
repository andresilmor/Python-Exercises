#Sabendo que um livro é caraterizado pelos seguintes dados: ISBN (e.g. 943-122334),
#título, autor, editora e ano em que foi publicado:
#   a. Crie a classe Livro.
#   b. Deverá ser possível criar livros indicando o valor de todos os seus atributos.
#   c. Implemente um método para imprimir todos os atributos de um dado livro
#   d. Crie um objeto do tipo livro e teste o que foi implementado nas alíneas
#      anteriores.
#   e. Crie, da forma que considerar mais adequada, uma “biblioteca de 5 livros”.
#   f. Preencha a “biblioteca de Livros” com dados provenientes do utilizador.
#   g. Implemente um método para listar todos os livros (e os seus dados) de toda a
#      biblioteca.
#   h. Implemente um método para pesquisar um dado livro através do seu ISBN. Caso
#      este seja encontrado, deverá aparecer a listagem das suas características.
#   i. Crie um objeto do tipo livro de nome “meuLivro” que seja uma cópia de um
#      objeto (à sua escolha) existente na biblioteca de livros. Use o método
#      implementado na alínea c. para verificar que a cópia foi efetuada com sucesso.

class Livro:
    def __init__(self,ISBN,Titulo,Autor,Editora,Ano):
        self.__ISBN=ISBN
        self.__Titulo=Titulo
        self.__Autor=Autor
        self.__Editora=Editora
        self.__Ano=Ano

    def LIVshow(self):
        print('Titulo: %s' %self.__Titulo)
        print('Autor: %s' %self.__Autor)
        print('Editora: %s' %self.__Editora)
        print('Ano: %s' %self.__Ano)
        print('ISBN: %s' %self.__ISBN)

    def getISBN(self):
        return self.__ISBN

    def getALL(self):
        return self.__Titulo, self.__Autor, self.__Editora, self.__Ano, self.__ISBN

def BIBLIOreg():
    listagem=[None]*5
    ano=-1
    for i in range(0,5):
        isbn=str(input('ISBN: '))
        tit=str(input('Titulo: '))
        aut=str(input('Autor: '))
        edi=str(input('Editora: '))
        while ano<0:
            try:
                ano=int(input('Ano: '))
                while ano<0:
                    ano=int(input('Ano Inválido!\nAno: '))
            except ValueError:
                print('Não foi inserido um número.')
        liv=Livro(isbn,tit,aut,edi,ano)
        ano=-1
        listagem[i]=liv
        print('-:-'*60)
    return listagem

def BIBLIOshow(lista):
    for i in range(0,5):
        lista[i].LIVshow()
        print('-'*80)

def BIBLIOsearch(lista):
    pro=(str(input('Indique o ISBN do livro que procura:\n')))
    for i in range(0,5):
        pesq=lista[i].getISBN()
        if pesq==pro:
            lista[i].LIVshow()

def BIBLIOcop(lista):
    cop=str(input('Indique o ISBN do livro que quer fazer cópia: '))
    cont=0
    for i in range(0,5):
        isb=lista[i].getISBN()
        if isb==cop:
            x=lista[i]
            cont+=1
    if cont==0:
        print('Não foi encontrado nenhum livro com esse ISBN.')
    elif cont>=2:
        print('ERRO! Foram encontrados vários livros com esse ISBN.')
    elif cont==1:
        return x
    elif cont!=1:
        copia='Não foi feita nenhuma cópia'
        return copia

def menu(biblio):
    print('-'*80)
    while True:
        copia=None
        opc=str(input('Qual opção quer?\n'
                   'A.Criar nova biblioteca;\n'
                   'B.Mostrar Biblioteca;\n'
                   'C.Procurar Livro;\n'
                   'D.Fazer Cópia dum livro;\n'
                   'E.Mostrar Cópia;\n'
                   'F.Terminar;\n'
                   'Opção: '))
        while opc not in 'AaBbCcDdEeFf':
            opc=str(input('Opção Inválida!\nOpção: '))
        if opc in 'Aa':
            biblio=BIBLIOreg()
            menu(biblio)
            return biblio
        elif opc in 'Bb':
            BIBLIOshow(biblio)
            menu(biblio)
        elif opc in 'Cc':
            BIBLIOsearch(biblio)
            menu(biblio)
        elif opc in 'Dd':
            copia=BIBLIOcop(biblio)
            menu(biblio)
        elif opc in 'Ee':
            copia.LIVshow()
        elif opc in 'Ff':
            print('Programa Terminado')
            break

biblio=BIBLIOreg()
menu(biblio)



