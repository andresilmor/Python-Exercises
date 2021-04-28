#Desenvolva um programa capaz de ler três números inteiros e dizer qual dos três é
#o maior (o programa deverá prever a possibilidade de os três números serem iguais.

def maior():
    lista=[None]*3
    try:
        lista[0]=int(input('Indique o 1º número: '))
        lista[1]=int(input('Indique o 2º número: '))
        lista[2]=int(input('Indique o 3º número: '))
    except ValueError:
        print('Não foi inserido um número.')
    if lista[1]<lista[0]>lista[2] or lista[0]==lista[1]>lista[2] or lista[0]==lista[2]>lista[1]:
        print('O número %d é o maior.' %lista[0])
    elif lista[0]<lista[1]>lista[2] or lista[1]==lista[0]>lista[2] or lista[1]==lista[2]>lista[1]:
        print('O número %d é o maior.' %lista[1])
    elif lista[1]<lista[2]>lista[0] or lista[2]==lista[1]>lista[0] or lista[2]==lista[0]>lista[1]:
        print('O número %d é o maior.' %lista[2])
    else:
        print('Os três números são iguais.')

maior()