#Desenvolva um algoritmo que faça a leitura de um número inteiro positivo (>=2) e
#que diga se o número fornecido é ou não um número primo (um número primo é
#aquele que só tem dois divisores: ele próprio e o número 1).

def primos():
    try:
        num=int(input('Indique um número: '))
        while num<2:
            num=int(input('Número Inválido!\nIndique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    cont=0
    for i in range(1,num+1):
        if num%i==0:
            cont=cont+1
    if cont==2:
        print('O número %d é primo.' %num)
    else:
        print('O número %d não é primo.' %num)

primos()