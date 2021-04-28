#Desenvolver um programa capaz de ler um número inteiro do teclado e que
#apresente a tabuada de multiplicação desse número.

def tabuada():
    try:
        num=int(input('Indique  um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    for i in range(1, 11):
        print('%d x %d = %d' %(num, i, num*i))

tabuada()