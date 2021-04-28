#Suponhamos que temos um lote de artigos, cada qual com um determinado preço,
#e que pretendíamos fazer uma atualização dos preços desses artigos todos
#segundo a mesma taxa ou percentagem. Por exemplo, consideremos os seguintes
#5 artigos com os respetivos preços em Euros:
#Ref Artigo:     0       1       2       3       4
#Preço:         200     250     300     350     400
#Pretende-se uma função que resolva a situação descrita atrás, considerando que se
#possui 50 artigos com referências de 0 a 49 e um preço inicial qualquer (poderá
#utilizar uma forma de preenchimento automático dos 50 valores ao invés de os
#solicitar ao utilizador).

def alteraValor():
    from random import randint
    produtos=[None]*10 #o espaços servem de referência.
    print('-'*77)
    for i in range(0,10):
        valor=randint(10,500)
        produtos[i]=valor
        print('%.2f' %produtos[i], end='  ')
    try:
        perc=float(input('\nIndique a percentagem: '))
        while perc<0:
            perc=float(input('Número Inválido!\nIndique a percentagem: '))
    except ValueError:
        print('Não foi inserido um número.')
    opc=str(input('É para aumentar[A] ou diminuir[D]? '))
    while opc not in 'AaDd':
        opc=str(input('Opção Inválida!\nÉ para aumentar[A] ou diminuir[D]? '))
    print('-' * 77)
    if opc in 'Aa':
        for i in range(0,10):
            pre=((perc*produtos[i])/100)+produtos[i]
            produtos[i]=pre
            print('%.2f' %produtos[i], end='  ')
    elif opc in 'Dd':
        for i in range(0,10):
            pre=produtos[i]-((perc*produtos[i])/100)
            produtos[i]=pre
            print('%.2f' %produtos[i], end='  ')

alteraValor()