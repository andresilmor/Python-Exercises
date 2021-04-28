#Desenvolver um algoritmo que mostre os números de 1 a 20.
#Altere o algoritmo anterior de forma a mostrar os números de 25 a 50.
#Altere o algoritmo anterior para que o intervalo de números a mostrar seja
#fornecido pelo utilizador.

def shownum():
    try:
        n1=int(input('Indique o primeiro número: '))
        n2=int(input('Indique o segundo número: '))
    except ValueError:
        print('Não foi inserido um número.')
    if n1 < n2:
        for i in range(n1,n2+1):
            print(i, end=' ')
    elif n1 > n2:
        for i in range(n1,n2-1,-1):
            print(i, end=' ')

shownum()