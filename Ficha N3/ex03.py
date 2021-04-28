#Desenvolver um programa que calcule o salário semanal a pagar a um empregado,
#tendo em atenção que todas as horas que este trabalha para além das 40 horas
#serão pagas a dobrar. O programa recebe do utilizador os valores de horas
#trabalhadas e o valor do salário por hora.

def salario():
    try:
        sal=float(input('Indique o pagamento por hora: '))
        while sal<0:
            sal=float(input('Número Inválido!\nIndique o pagamento por hora: '))
        hor=int(input('Indique o número de horas de trabalho: '))
        while hor<0:
            hor=int(input('Número Inválido!\nIndique o número de horas de trabalho: '))
    except ValueError:
        print('Não foi inserido um número.')
    if hor<=40:
        print('Pelas %d horas de trabalho, receberá %.2fEur.' %(hor, hor*sal))
    elif hor>40:
        print('Pelas %d horas de trabalho, receberá %.2Eur.' %(hor, ((sal*40)+((hor-40)*2))))

salario()