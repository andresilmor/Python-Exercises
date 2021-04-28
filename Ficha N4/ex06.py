#Desenvolver uma função que leia e devolva um valor inteiro lido do teclado. A
#função deverá também receber dois valores inteiros (limINF e LimSUP) e garantir
#que o valor devolvido (aceite) esteja entre [limINF, limSUP].

def valor():
    try:
        limINF=int(input('Insira o limite inferior: '))
        limSUP=int(input('Insira o limite superior: '))
        while limSUP<limINF or limINF==limSUP:
            limSUP=int(input('O limSuperior indicado é inválido!\nInsira o limite superior: '))
        num=int(input('Insira um número: '))
        while num>limSUP or num<limINF:
            num=int(input('Número Inválido!\nInsira um número: '))
    except ValueError:
        print('Não foi inserido um número.')
    print('O número %d é válido.' %num)

valor()