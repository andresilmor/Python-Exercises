#Desenvolver uma função que seja capaz de calcular e devolver a soma dos divisores
#próprios de um número N, sendo N um valor fornecido à função.
#Divisores próprios de N são todos os divisores de N, com exceção de N.
#Exemplo: divisores próprios de 16 são 1, 2, 4, 8.

def soma3():
    try:
        num=int(input('Indique um número: '))
        while num<0:
            num=int(input('Número Inválido!\nIndique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    divisores=[]
    for i in range(1,num):
        if num%i==0:
            divisores.append(i)
    soma=0
    for i in divisores:
        soma+=i
    print('A soma de todos os divisores de %d, deu %d.' %(num, soma))
    print('Sendo os divisores: ', end=' ')
    print(divisores)

soma3()