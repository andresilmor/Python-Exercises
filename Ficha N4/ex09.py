#Desenvolver uma função capaz de calcular o fatorial de um número recebido como
#argumento.

def mulfar():
    try:
        num=int(input('Indique um número: '))
        while num<0:
            num=int(input('Número Inválido!\nIndique um número: '))
    except ValueError:
        print('Não foi inserido um número!')
    multi=1
    for i in range(num,1,-1):
        multi*=i
        print('%d x' %(i), end=' ')
    print('1 = %d' %(multi))

mulfar()