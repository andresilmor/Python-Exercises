#Desenvolver um algoritmo que faça a leitura de um número inteiro positivo e que,
#para esse número, mostre todos os seus divisores.

def divisor():
    try:
        num=int(input('Indique um número: '))
        while num<0:
            num=int(input('Número Inválido!\nIndique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    for i in range(1,num+1):
        if num%i==0:
            print(i, end=' ')

divisor()