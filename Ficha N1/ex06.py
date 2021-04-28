#Ler um número inteiro e, no caso desse número se encontrar dentro do intervalo
#[100,999], deverá dizer se esse número é ou não uma capicua. No caso do número
#se encontrar fora do intervalo, o algoritmo deverá dizer apenas se o número é <100
#ou se é >999.

def num100_999():
    try:
        num=int(input('Insira um número entre 100 e 999: '))
    except ValueError:
        print('Não foi inserido um número')
    if num>999:
        print('O número %d é maior que 999.' %num)
    elif num<100:
        print('O número %d é menor que 100.' %num)
    else:
        return num

def capicua(num):
    numS=str(num)
    if numS[:1]==numS[-1:]:
        print('O número %d é capicua.' %num)
    else:
        print('O número %d não é capicua.' %num)

num=num100_999()
capicua(num)