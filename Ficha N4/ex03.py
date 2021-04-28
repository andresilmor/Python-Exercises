#Desenvolver um programa capaz de verificar se um dado número inteiro N (lido do
#teclado e dentro do intervalo [2,10000] é ou não primo. De seguida, altere o
#programa para que indique quantos quais são os números primos pertencentes ao
#intervalo [2,10000].

def primo1():
    try:
        num=int(input('Indique um número: '))
        while num<2 or num>10000:
            num=int(input('Número Inválido!\nIndique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    if num%2==0:
        print('O número %d é primo.' %num)
    else:
        print('O número %d não é primo.' %num)

def primoTODOS():
    lista=[]
    for i in range(2,10001):
        if i%2==0:
            lista.append(i)
    print(lista)

opc=0
while opc<1 or opc>2 :
    try:
        opc=int(input('Indique qual das opções quer:\n'
                      '1. Ver se número é primo.\n'
                      '2. Ver todos números primos.\n'
                      'Opção: '))
    except ValueError:
        print('Não foi inserido um número.')
if opc==1:
    primo1()
elif opc==2:
    primoTODOS()
