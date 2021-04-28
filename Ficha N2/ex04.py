#Desenvolver um algoritmo que leia dois números inteiros (N1 e N2) e que mostre
#todos os números entre N1 e N2 que sejam múltiplos de 4.

def mult4():
    try:
        n1=int(input('Indique o primeiro número: '))
        n2=int(input('Indique o segundo número: '))
    except ValueError:
        print('Não foi inserido um número.')
    if n1>n2:
        for i in range(n2,n1+1):
            if i%4==0:
                print(i, end=' ')
    elif n2>n1:
        for i in range(n1,n2+1):
            if i%4==0:
                print(i, end=' ')

mult4()