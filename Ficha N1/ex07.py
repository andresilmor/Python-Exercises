#Calcular o salário semanal a pagar a um empregado, tendo em atenção que todas
#as horas que este trabalha para além das 40 horas serão pagas a dobrar. O
#algoritmo/programa recebe do utilizador os valores de horas trabalhadas e o valor
#do salário por hora.

def salario():
    try:
        hor=int(input('Indique o número de horas de trabalho: '))
        while hor<0:
            hor=int(input('Número Inválido!\nIndique o número de horas de trabalho: '))
        sal=float(input('Indique o pagamento/hora: '))
        while sal<0:
            sal=float(input('Número Inválido!\nIndique o pagamento/hora: '))
    except ValueError:
        print('Não foi inserido um número.')
    if hor<=40:
        print('O salário semanal será de %.2fEur.' %(hor*sal))
    elif hor>40:
        print('O salário semanal será de %.2fEur.' %((sal*40)+((hor-40)*sal*2)))

salario()