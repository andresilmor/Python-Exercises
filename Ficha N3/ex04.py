#Desenvolver um programa capaz de ler do teclado um número inteiro, garantindo
#que esteja entre 10 e 15 e que depois mostre o quadrado e o cubo desse número.

def numquad(num):
    print('O número %d ao quadrado é %d.' %(num, num**2))

def numcub(num):
    print('O número %d ao cubo é %d.' %(num, num**3))

def num():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    return num

num=num()
numquad(num)
numcub(num)
