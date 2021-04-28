#Desenvolver um programa que leia números inteiros fornecidos pelo utilizador até
#que o utilizador digite um número que esteja no intervalo [100,999]. Para esse
#número, o algoritmo deverá dizer se é ou não uma capicua.

def capicua():
    try:
        num=int(input('Insira um número: '))
        while num<100 or num>999:
            print('Número Inválido!\nInsira um número: ')
    except ValueError:
        print('Não foi inserido um número.')
    numS=str(num)
    if numS[-1:]==numS[:1]:
        print('O número %d é capicua.' %num)
    else:
        print('O número %d não é capicua.' %num)

capicua()