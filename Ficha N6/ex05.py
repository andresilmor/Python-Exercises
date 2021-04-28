#Implemente um programa que permita ler uma série de números, até que o utilizador
#digite zero ou que o número de valores lidos ultrapasse NMAX=10. O programa deve
#indicar o maior número inserido e mostrar todos os valores lidos por ordem contrária
#à qual foram inseridos.

def numeros():
    lista=[]
    num=1
    cont=0
    while cont<10:
        try:
            num=int(input('Indique o %dº número: ' %(cont+1)))
        except ValueError:
            print('Não foi inserido um número.\nO programa não irá funcionar.')
            print('-/-'*70)
        if num==0:
            break
        lista.append(num)
        cont+=1
    mai=lista[0]
    for i in lista:
        if i>mai:
            mai=i
    print('O maior número foi %d.' %mai)
    print(lista)
    listaINV=[]
    pos=cont-1 #A contagem contou do 1 ao (exemplo) 4 no entanto a lista começa a contar a partir do 0,
               #ou seja do 0 ao 3
    for i in range(0,cont):
        ty=lista[pos]
        listaINV.append(ty)
        pos-=1
    print(listaINV)

numeros()

