#Leia as medidas de um determinado sólido retangular, comprimento e largura da
#base e a altura. Posteriormente, calcular o volume do sólido e dizer se se trata de
#um cubo ou se é um paralelepípedo.

def medidas():
    try:
        alt=float(input('Indique a altura do sólido: '))
        while alt<0:
            alt=float(input('Medida Inválida!\nIndique a altura do sólido: '))
        com=float(input('Indique o comprimento da base do sólido: '))
        while com<0:
            com=float(input('Medida Inválida!\nIndique o comprimento da base do sólido: '))
        lar=float(input('Indique a largura da base: '))
        while lar<0:
            lar=float(input('Media Inválida!\nIndique a largura da base do sólido: '))
    except ValueError:
        print('Não foi inserido um número.')
    if alt==com==lar:
        print('As medidas do sólido inserido correspondem a um cubo,\ne o seu volume é %.2f.' % (alt * lar * com))
    else:
        print('As medidas do sóldido inserido correspondem a um paralelepipedo,\ne o seu volume é %.2f.' % (alt * lar * com))

medidas()