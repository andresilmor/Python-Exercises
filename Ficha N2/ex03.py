#Desenvolver um algoritmo capaz de ler 7 números inteiros e no final apresentar
#qual o valor máximo e o valor mínimo introduzidos. Acrescente ao algoritmo a
#funcionalidade que lhe permita apresentar a média dos valores lidos.

def setnum():
    try:
        num=int(input('Indique o 1º número: '))
    except ValueError:
        print('Não foi inserido um número.')
    mai=min=num
    for i in range(0,6):
        try:
            num=int(input('Indique o %dº número: ' %(i+2)))
        except ValueError:
            print('Não foi inserido um número.')
        if num > mai:
            mai=num
        elif num < min:
            min=num
    print('O maior número inserido foi %d, e o menor foi %d.' %(mai, min))

setnum()