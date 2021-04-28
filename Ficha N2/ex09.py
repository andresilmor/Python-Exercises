#Desenvolver um algoritmo capaz de calcular qual o máximo e qual o mínimo valor
#de uma série de números inteiros positivos lidos do teclado cuja marca de fim é -1.

def numMinMaX():
    try:
        num=int(input('Insira um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    max=min=num
    while num!=-1:
        try:
            num=int(input('Insira um número: '))
        except ValueError:
            print('Não foi inserido um número.')
        if num==-1:
            break
        elif num<min:
            min=num
        elif num>max:
            max=num
    print('O maior número inserido foi o %d e o menor foi %d.' %(max, min))

numMinMaX()


