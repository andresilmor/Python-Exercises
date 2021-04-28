#Desenvolver um algoritmo que leia um número inteiro e que apresente a tabuada
#de multiplicação desse número.

def tabuada():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    for i in range(0,10):
        print('%d x %d = %d' %(num, i+1, (i+1)*num))

tabuada()
