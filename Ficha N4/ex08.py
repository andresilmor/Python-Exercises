#Desenvolver uma função que recebe as 3 notas de um aluno e uma letra. Se a letra
#for A, é calculada e devolvida a média aritmética das notas do aluno, se for P, a
#função calcula a média ponderada (pesos: 50%, 30% e 20%).
#Nota: Se não for fornecida qualquer letra, a função deverá assumir que se trata
#da letra A.  #QUE MERDA E ESSA DE MEDIA PONDERAS!!!!!!!!

def media():
    notas=[None]*3
    try:
        for i in range(0,3):
            notas[i]=float(input('Indique a %dº nota: ' %(i+1)))
            while notas[i]<0 or notas[i]>20:
                notas[i]=float(input('Nota Inválida!\nIndique uma nota: '))
    except ValueError:
        print('Não foi inserido um número.')
    opc=str(input('Indique qual média quer vêr:\n'
                  'A.Média Artimética\n'
                  'P.Média Ponderada\nOpção: '))
    while opc not in 'AaPp ':
        opc=str(input('Opção Inválida!\nOpção: '))
    if opc in 'Aa' or opc in' ':
        med=(notas[0]+notas[1]+notas[2])/3
        print('A média é %.2f.' %(med))
    elif opc in 'Pp':
        med=(notas[0]+notas[1]+notas[2])/3
        pes0=(notas[0]*100)/med
        pes1=(notas[1]*100)/med
        pes2=(notas[2]*100)/med
        print('A média é %.2f,\n'
              'sendo que a nota %.2f têm o peso de %.2f\n'
              'a nota %.2f têm o peso de %.2f\n'
              'e a nota %.2f têm o peso de %.2f.' %(med, notas[0], pes0, notas[1], pes1, notas[2], pes2))

media()
