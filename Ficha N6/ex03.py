#Implemente uma função capaz de receber uma string e retornar essa string invertida

def invertSTR():
    string=str(input('Escreva uma frase/palavras:\n'))
    print('-'*80)
    cont=cont2=0
    for i in string:
        cont+=1
        cont2+=1
    lista=[None]*cont
    for i in string:
        lista[cont-1]=i
        cont-=1
    inv=''
    for i in range(0,cont2):
        inv=inv+lista[i]
    print(inv)

invertSTR()