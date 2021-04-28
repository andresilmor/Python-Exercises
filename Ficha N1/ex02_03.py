#Desenvolver um algoritmo que leia o preço base de um determinado produto e
#calcule o seu preço de venda ao público (ou seja, preço base acrescido da taxa de
#IVA a 23%).
#Altere o algoritmo anterior para que o valor da taxa de IVA seja também um valor
#fornecido pelo utilizador.

def IVA():
    try:
        iva=float(input('Indique o valor do IVA: '))
        pre_Base=float(input('Indique o preço do produto: '))
    except ValueError:
        print('Não foi inserido um número.')
    res=((iva*pre_Base)/100)+pre_Base
    print('Com o IVA de %.2f por cento, o preço do produto que era %.2fEur,\npassou a ser %.2fEur.' %(iva, pre_Base, res))

IVA()