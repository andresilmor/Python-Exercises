#Implemente um programa que faça a leitura de uma string e a leitura de um carater e
#depois apresente o número de ocorrências desse caracter na string inicial.

def contSTR():
    sring=str(input('Escreva uma frase/palavra:\n'))
    print('-'*80)
    let=str(input('Indique uma letra: '))
    while let not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUWXYZ':
        let=str(input('Letra Inválida!\nInsique uma letra: '))
    cont=0
    for i in sring:
        if i==let:
            cont+=1
    print('Foram encontrados %d \'%s\'.' %(cont, let))

contSTR()