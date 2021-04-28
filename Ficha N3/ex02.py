#Desenvolver um programa que determine se um determinado ano é ou não
#bissexto (um ano é bissexto se for divisível por 4 E não for divisível por 100 OU for
#divisível por 400).

def anobi():
    try:
        ano=int(input('Indique um ano: '))
        while ano<0:
            ano=int(input('Ano Inválido!\nIndique um ano: '))
    except ValueError:
        print('Não foi inserido um número.')
    if ano%4==0:
        print('O ano %d é bissexto.' %ano)
    elif ano%4!=0:
        print('O ano %d não é bissexto.' %ano)

anobi()