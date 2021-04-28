#Desenvolver um programa que vá lendo do teclado números inteiros até que a
#soma desses números atinja ou ultrapasse um limite máximo indicado previamente
#pelo utilizador. O algoritmo deverá no final dizer quantos foram os valores
#digitados.

def soma2():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    soma=cont=0
    while soma<num:
        cont+=1
        soma+=cont
    print('Foram inserido ao todo %d números.' %cont)

soma2()