#Implemente um programa que faça a leitura de valores para uma lista com as
#classificações (inteiras) de uma turma de 20 alunos. Acrescente ao programa as
#seguintes funcionalidades (usando funções):
#a) Calcular a média das notas.
#b) Calcular o somatório de todos as notas positivas do vetor.
#c) Calcular a menor e a maior nota.
#d) Ordenar o vetor por ordem decrescente.
#e) Indicar quantas classificações iguais, a uma classificação recebida como
#argumento, existem na lista de notas

def notas():
    lista=[None]*20
    for i in range(0,20):
        try:
            num=int(input('Insira a %dº nota: ' %(i+1)))
            while num>20 or num<0:
                num=int(input('Nota Inválida!\nInsira a %dº' %(i+1)))
        except ValueError:
            print('Não foi inserido um número.')
        lista[i]=num
    return lista

def media(lista):
    med=0
    for i in range(0,20):
        med+=lista[i]
    med=med/20
    print('A média da turma é %.2f.' %med)

def notasPOS(lista):
    soma=0
    for i in range(0,20):
        if lista[i]>=10:
            soma+=lista[i]
    print('A soma de todas as notas positivas deu %d.' %soma)

def menMai(lista):
    men=mai=lista[2]
    for i in range(0,10):
        if lista[i]<men:
            men=lista[i]
        elif lista[i]>mai:
            mai=lista[i]
    print('A menor nota é %d e a maior nota foi %d.' %(men, mai))

def ordenarDECRE(lista):
    for i in range(0, 10):
        for j in range(i + 1, 8):
          if lista[j] > lista[i]:
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    print(lista)

def search(lista):
    try:
        num=int(input('Insira a nota pela qual quer procurar: '))
        while num>20 or num<0:
            num=int(input('Nota inválida!\nInsira a nota pela qual quer procurar: '))
    except ValueError:
        print('Não foi inserido um número.')
    cont=0
    for i in range(0,20):
        if lista[i]==num:
            cont+=1
    print('Foram encontrados %d \'%d\'.' %(cont, num))

def menu(lista):
    opc=str(input('Indique qual opção quer:\n'
              'a) Calcular a média das notas.\n'
              'b) Calcular o somatório de todos as notas positivas do vetor.\n'
              'c) Calcular a menor e a maior nota.\n'
              'd) Ordenar o vetor por ordem decrescente.\n'
              'e) Indicar quantas classificações iguais, a uma classificação recebida como\n'
              '   argumento, existem na lista de notas\n'
              'Opção: '))
    while opc not in 'AaBbCcDdEe':
        opc=str(input('Opção Inválida!\nOpção: '))
    if opc in 'Aa':
        media(lista)
        print('-'*80)
        menu(lista)
    elif opc in 'Bb':
        notasPOS(lista)
        print('-'*80)
        menu(lista)
    elif opc in 'Cc':
        menMai(lista)
        print('-'*80)
        menu(lista)
    elif opc in 'Dd':
        ordenarDECRE(lista)
        print('-'*80)
        menu(lista)
    elif opc in 'Ee':
        search(lista)
        print('-'*80)
        menu(lista)

lista=notas()
menu(lista)
