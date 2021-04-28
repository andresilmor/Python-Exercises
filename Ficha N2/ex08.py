#Elabore um algoritmo que dada uma sequência de números inteiros terminada por
#0, calcule a percentagem correspondente aos valores superiores a 10.
#Nota: O 0 não deverá contar para efeitos de cálculo!

def numMai10():
    num=-1
    cont=0
    while num!=0:
        try:
           num=int(input('Indique um número: '))
        except ValueError:
           print('Não foi inserido um número.')
        if num>10:
            cont=cont+1
    print(cont)

numMai10()