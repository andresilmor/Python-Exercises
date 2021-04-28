#Desenvolva um programa que faça a leitura de um número positivo menor do que
#24 (garantindo que assim seja) e em seguida mostre o quadrado e o cubo de todos
#os números entre 1 e o valor lido inclusive.

def num():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    return num

def cubo(num):
    for i in range(1,num+1):
        print('O número %d ao cubo é %d.' %(i, i**3))

def quadrado(num):
    for i in range(1, num+1):
        print('O número %d ao quadrado é %d.' %(i, i**2))

print('-'*30)
num=num()
print('-'*30)
cubo(num)
print('-'*30)
quadrado(num)
print('-'*30)