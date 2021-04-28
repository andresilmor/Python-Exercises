#Desenvolver um programa capaz de ler 5 números inteiros e no final apresentar a
#soma desses valores. Altere, depois, o programa por forma a mostrar também a
#média dos números lidos. Bónus: Mostra números

def soma():
    lista=[]
    soma=0
    for i in range(5):
        try:
            num=int(input('Indique um número: '))
        except ValueError:
            print('Não foi inserido um número.')
        soma+=num
        lista.append(num)
    print('A soma dos números', lista, 'deu %d,\ne a média foi %.2f.' %(soma, soma/5))

soma()