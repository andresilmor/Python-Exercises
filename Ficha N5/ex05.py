#Tendo NElem como uma Lista de 25 elementos do tipo Inteiro, desenvolva um
#programa que faça a leitura de N elementos para essa Lista sendo pedido ao
#utilizador o valor de N (num máximo de 25). De seguida desenvolva:
#a) Uma função para fazer a apresentação dos elementos dessa lista.
#b) uma função que calcule o menor elemento.
#c) uma função para calcular a média dos elementos da lista.
#d) uma função que devolva o somatório de todos os números positivos da lista.
#e) uma função que devolva o somatório de todos os números negativos da lista.
#f) uma função que receba como argumento, para além da lista, um inteiro e
#devolva quantas vezes é que esse número aparece na lista.
#g) uma função que devolva o somatório de todos os números pares da lista.

def criarLista():
    lista=[None]*10
    for i in range(0,10):
        try:
            lista[i]=int(input('Indique o %dº número: ' %(i+1)))
        except ValueError:
            print('Não foi inserido um número.')
    return lista

def menorElem(lista):
    men=lista[2]
    for i in range(0,10):
        if lista[i]<men:
            men=lista[i]
    print('O menor número é %d.' %men)

def media(lista):
    med=0
    for i in range(0,10):
        med+=lista[i]
    med=med/10
    print('A média é %.2f.' %med)

def somaPOS(lista):
    soma=0
    for i in range(0,10):
        if i>0:
            soma+=lista[i]
    print('A soma de todos os números positivos deu %d.' %soma)

def somaNEG(lista):
    soma=0
    for i in range(0,10):
        if i<0:
            soma+=lista[i]
    print('A soma de todos os números negativos deu %d.' %soma)

def search(lista):
    try:
        num=int(input('Indique pelo número que quer procurar: '))
    except ValueError:
        print('Não foi inserido um número.')
    cont=0
    for i in range(0,10):
        if lista[i] == num:
            cont+=1
    print('A todo foram encontrados %d \'%d\'.' %(cont, num))

def somaPARES(lista):
    soma=0
    for i in range(0,10):
        if lista[i]%2==0:
            soma+=lista[i]
    print('A soma de todos os números pares deu %d.' %soma)

def menu():
    opc=str(input('Indique a opção que deseja:\n'
                  'a) Uma função para fazer a apresentação dos elementos dessa lista.\n'
                  'b) uma função que calcule o menor elemento.\n'
                  'c) uma função para calcular a média dos elementos da lista.\n'
                  'd) uma função que devolva o somatório de todos os números positivos da lista.\n'
                  'e) uma função que devolva o somatório de todos os números negativos da lista.\n'
                  'f) uma função que receba como argumento, para além da lista, um inteiro e\n'
                  '   devolva quantas vezes é que esse número aparece na lista.\n'
                  'g) uma função que devolva o somatório de todos os números pares da lista.\n'
                  'Opção: '))
    while opc not in 'AaBbCcDdEeFfGg':
        opc=str(input('Opção Inválida!\nOpção: '))
    if opc in 'Aa':
        print(lista)
        print('-' * 80)
        menu()
    elif opc in 'Bb':
        menorElem(lista)
        print('-' * 80)
        menu()
    elif opc in 'Cc':
        media(lista)
        print('-' * 80)
        menu()
    elif opc in 'Dd':
        somaPOS(lista)
        print('-' * 80)
        menu()
    elif opc in 'Ee':
        somaNEG(lista)
        print('-' * 80)
        menu()
    elif opc in 'Ff':
        search(lista)
        print('-' * 80)
        menu()
    elif opc in 'Gg':
        somaPARES(lista)
        print('-' * 80)
        menu()

print('-'*80)
lista=criarLista()
print('-'*80)
menu()