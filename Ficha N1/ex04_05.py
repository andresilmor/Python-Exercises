#Ler dois números e dizer qual deles é o maior. O algoritmo também deverá prever
#a situação de serem iguais.
#Ler três números e dizer qual deles é o maior.

def numMai():
    numL=[None]*3
    for i in range(0,3):
        try:
         numL[i]=int(input('Indique o %dº número: ' %(i+1)))
        except ValueError:
            print('Não foi inserido um número.')
            break
    if numL[2]<numL[0]>numL[1] or numL[0]==numL[1]>numL[2] or numL[0]==numL[2]>numL[1]:
        print('O número %d é o maior.' %numL[0])
    elif numL[0]<numL[1]>numL[2] or numL[1]==numL[2]>numL[0] or numL[1]==numL[0]>numL[2]:
        print('O número %d é o maior.' %numL[1])
    elif numL[1]<numL[2]>numL[0] or numL[2]==numL[1]>numL[0] or numL[2]==numL[0]>numL[1]:
        print('O número %d é o maior.' %numL[2])
    else:
        print('Os três números são iguais.')

numMai()