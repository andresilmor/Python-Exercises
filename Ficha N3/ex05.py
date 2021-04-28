#Desenvolver um programa que, calcule a percentagem de números múltiplos de 4,
#de uma série de números digitados pelo utilizador. A apresentação do resultado
#dever ser feita após o utilizador inserir o número zero (não contando este último
#para o cálculo da percentagem). Bónus: Dizer quais.

def mul4():
    num=-1
    cont=0
    lista=[]
    while num!=0:
        try:
            num=int(input('Inserir um número: '))
        except ValueError:
            print('Não foi inserido um número.')
        if num%4==0:
            cont+=1
            if num!=0:
                lista.append(num)
    print('Foram inseridos ao todo %d números múltiplos de 4.' %(cont-1))
    print('Sendo eles', end=' ')
    print(lista)

mul4()
