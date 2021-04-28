#Desenvolver um algoritmo calcule o somatório de 1 até um número N, sendo N um
#valor fornecido pelo utilizador.

def somatorio():
    try:
        num=int(input('Indique um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    calc=0
    for i in range(0,num+1):
        calc=calc+i
    print(calc)

somatorio()