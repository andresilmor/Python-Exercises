#EUROMILHÕES: implemente um programa que permita preencher e posteriormente
#mostrar uma lista de 5 inteiros com números aleatórios de 1 a 50. O programa deve no
#final perguntar se o utilizador deseja calcular nova chave.

def sorteio():
    lista=[None]*5
    from random import randint
    for i in range(0,5):
        num=randint(1,50)
        while num in lista:
            num=randint(1,50)
        lista[i]=num
    print('Estes são os números sorteados: ')
    for i in range(0,5):
        print(lista[i], end=' ')
    print('\n')
    print('-'*80)


opc='S'
while opc not in 'Nn':
    sorteio()
    opc=input('Deseja repetir? [S/N]\n')
    while opc not in 'SsNn':
        opc = input('Opção Inválida!\nDeseja repetir? [S/N]\n')
