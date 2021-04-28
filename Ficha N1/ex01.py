#Sabendo que 1€ são 200.482 escudos, escreva um algoritmo que calcule, em euros,
#o valor de determinada quantia em escudos (fornecida pelo utilizador).

def escConv():
    try:
        esc=float(input('Indique a quantia (em escudos) que quer converter:\n'))
    except ValueError:
        print('Não foi inserido um número.')
    fix=200.482
    eur=esc/fix
    print('A quantia, %.2fEsc, equivale a %.2fEur.' %(esc, eur))

escConv()