#Desenvolver uma função que receba como argumentos dois valores reais e proceda
#à sua troca.

def troca():
    try:
        num1=float(input('Indique um número: '))
        num2=float(input('Indique um segundo número: '))
    except ValueError:
        print('Não foi inserido um número.')
    print('Num1 = %.2f' %num1)
    print('Num2 = %.2f' %num2)
    numEX=num1
    num1=num2
    num2=numEX
    print('-'*20)
    print('Num1 = %.2f' %num1)
    print('Num2 = %.2f' %num2)

troca()