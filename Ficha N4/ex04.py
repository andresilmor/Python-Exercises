#Desenvolver um algoritmo que seja capaz de apresentar a lista de todos os divisores
#de um número inteiro positivo digitado pelo utilizador.

def divisores():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    lista=[]
    for i in range(1,num+1):
        if num%i==0:
            lista.append(i)
    print(lista)

divisores()