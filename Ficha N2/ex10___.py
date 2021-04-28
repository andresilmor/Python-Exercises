#Desenvolver um algoritmo que leia um número inteiro no intervalo [10,99] e diga
#se o correspondente invertido desse número é múltiplo de 7.
#Exemplo: valor lido 12, invertido fica 21, 21 é múltiplo de 7.

def invert():
    try:
        num=int(input('Insira um número: '))
        while num>99 or num<10:
            num=int(input('Número Inválido!\nInsira um número: '))
    except ValueError:
        print('Não foi inserido um número.')


invert()