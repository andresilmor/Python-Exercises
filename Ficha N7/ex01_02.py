#Implemente um programa que faça sucessivas leituras de nomes completos de
#pessoas (introduzidos pelo utilizador) até que o utilizador decida inserir uma linha em
#branco/vazia. Os vários nomes inseridos deverão ser armazenados num ficheiro com o
#nome: pessoas.txt
#Tendo por base o ficheiro da questão 1, mostre o conteúdo do ficheiro na consola.

def REGnomes():
    ficheiro=open('pessoas.txt', 'a') #a escrever, w apagar e escrever, r ler
    text=0
    while text!='':
        text=str(input('Indique um nome:\n'))
        if text=='':
            break
        ficheiro.write(text+'\n')
    ficheiro.close()
    ficheiro=open('pessoas.txt','r')
    most=ficheiro.read()
    print(most)
    ficheiro.close()

REGnomes()