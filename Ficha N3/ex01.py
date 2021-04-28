#Desenvolver um algoritmo que faça a leitura de um número inteiro e indique se este
#é um número par ou ímpar.

def parimpar():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    if num%2==0:
        print('O número %d é par.' %(num))
    elif num%2!=0:
        print('O número %d é impar.' %num)

parimpar()