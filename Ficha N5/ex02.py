#Desenvolver um subprograma que recebe 3 valores inteiros e que os retorna
#ordenados por ordem crescente.

def ordenar():
    num=[None]*3
    for i in range(0,3):
        try:
            num[i]=int(input('Indique o %dº número: ' %(i+1)))
        except ValueError:
            print('Não foi inserido um número.')
    n1=n2=n3=num[0]
    for i in num:
        if i<n1:
            n1=i
    for i in num:
        if i>n3:
            n3=i
    for i in num:
        if i<n3 and i>n1:
            n2=i
    if num[1]!=num[2]!=num[0]:
        print('%d < %d < %d' %(n1, n2, n3))
    elif num[2]==num[1]==num[0]:
        print('Os três números são iguais.')
    elif num[1]==num[2]<num[0]:
        print('%d < %d' %(n1,n3))
    elif num[2]==num[0]<num[1]:
        print('%d < %d' %(n2,n1))
    elif num[1]==num[0]<num[2]:
        print('%d < %d' %(n1,n2))

ordenar()