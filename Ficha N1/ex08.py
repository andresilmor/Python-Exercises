#Leia as medidas de um determinado sólido retangular, comprimento e largura da
#base e a altura. Posteriormente, calcular o volume do sólido e dizer se se trata de
#um cubo ou se é um paralelepípedo.

def solido():
    try:
        alt=float(input('Indique a altura do sólido: '))
        while alt<0:
            alt=float(input('Número Inválido!\nIndique a altura do sólido: '))
        com=float(input('Indique o comprimento da base: '))
        while com<0:
            com=float(input('Número Inválido!\nIndique o comprimento do sólido: '))
        lar=float(input('Indique a largura da base: '))
        while lar<0:
            lar=float(input('Número Inválid!\nIndique a largura da base: '))
    except ValueError:
        print('ão foi inserido um número.')
    if alt==com==lar:
        print('O sólido é um cubo.\nO seu volume é de %.2f' %(alt**3))
    else:
        print('O sóldido é um retângulo.\nO seu volume é %.2f.' %(alt*lar*com))

solido()