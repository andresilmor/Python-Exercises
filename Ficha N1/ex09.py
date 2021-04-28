#Desenvolver um algoritmo que permita calcular o peso ideal de uma determinada
#pessoa, sendo fornecidos os valores da altura (em metros) e sexo (M, F). O cálculo
#do peso ideal é feito segundo as seguintes fórmulas:
#à para homens: 72.7 x h - 58.0 ( h : altura em metros)
#à para mulheres: 62.1 x h - 44.7

def pesoIdeal():
    alt=-1
    while alt<0:
        try:
            alt=float(input('Indique a sua altura: '))
            while alt<0:
                alt=float(input('Número Inválido!\nIndique a sua altura: '))
        except ValueError:
            print('Não foi inserido um número.')
    sex=str(input('Indique o seu sexo [M/F]: '))
    while sex not in 'MmFf':
        sex=str(input('Info inválida!\nIndique o seu sexo [M/F]: '))
    if sex in 'Ff':
        print('O seu peso ideal é %.2fKg.' %((62.1*alt)-44.7))
    elif sex in 'Mm':
        print('O seu peso ideal é %.2fKg.' %((72.7*alt)-58.0))

pesoIdeal()