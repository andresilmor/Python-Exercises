#1. Sabendo que um dado software terá de ser criado para gerir as pessoas que
#“povoam” a EsACT (caraterizada por: morada) e que a EsACT tem várias
#pessoas. E que de entre essas pessoas temos:
#   - Alunos (caraterizados por: cc, nif, NumMec, curso, ano)
#   - Professores (caraterizados por: cc, nif, numFunc, departamento,
#     categoria, habilitações)
#Implemente, em Python, um programa capaz de:
#   i. Inserir alunos e professores
#   ii. Imprimir os dados de alunos e professores
#   iii. Pesquisar alunos por NumMec
#   iv. Pesquisar Professores por categoria
#   v. Pesquisar alunos e professores pelo cc

class EsACT:
    def __init__(self):
        self.__Alunos=[]
        self.__Professores=[]

    def ADDaluno(self,CC,NIF,NumMec,Curso,Ano):
        aluno=Aluno(CC,NIF,NumMec,Curso,Ano)
        self.__Alunos.append(aluno)
        print('Feito!')

    def ADDprofessor(self,CC,NIF,NumFunc,Departamento,Categoria,Habilitacoes):
        professor=Professor(CC,NIF,NumFunc,Departamento,Categoria,Habilitacoes)
        self.__Professores.append(professor)
        print('Feito!')

    def getAlunosLista(self):
        return self.__Alunos

    def getProfLista(self):
        return self.__Professores

    def showAlProf(self):
        opc = -1
        cont = 0
        while opc < 0:
            try:
                opc = int(input('1.Mostrar Professores\n'
                                '2.Mostrar Alunos\n'
                                '3.Mostrar Alunos e Professores\n'
                                'Opção:'))
                while opc < 1 or opc > 3:
                    opc = int(input('Opção Inválida! Opção: '))
            except:
                print('Não foi inserido um número.')
        if opc == 1:
            for objeto in self.__Professores:
                cla = objeto.getClasse()
                if cla == 'Professor':
                    cont += 1
                    objeto.PROFshow()
            if cont == 0:
                print('Não foi encontrado nenhum professor.')
        elif opc == 2:
            for objeto in self.__Alunos:
                cla = objeto.getClasse()
                if cla == 'Aluno':
                    objeto.ALUshow()
                    cont += 1
            if cont == 0:
                print('Não foi encontrado nenhum aluno.')
        elif opc == 3:
            cont=0
            for objeto in self.__Professores:
                cla = objeto.getClasse()
                if cla == 'Professor':
                    objeto.PROFshow()
                    cont+=1
            for objeto in self.__Alunos:
                cla = objeto.getClasse
                if cla == 'Aluno':
                    objeto.ALUshow()
                    cont+=1
            if cont==0:
                print('Não foi encontrado nenhum aluno/professor.')

    def searchALUNOnumMec(self):
        NumMec = cont = -1
        while NumMec < 0:
            try:
                NumMec = int(input('Indique o Número Mec do aluno que procura: '))
                while NumMec < 0:
                    NumMec = int(input('Número Inválido! Indique o Número Mec do aluno que procura: '))
            except ValueError:
                print('Não foi inserido um número.')
        for i in self.__Alunos:
            num=i.getNumMec
            if NumMec==num:
                i.ALshow()
                cont+=1
        if cont==0:
            print('Não foi encontrado nenhum aluno com esse número mec.')

    def searchPROFcat(self):
        cont=0
        cat=-1
        while cat<0:
            try:
                cat=int(input('Indique a Categoria do Professor que procura:\n'
                              ' 1.Professor\n'
                              ' 2.Professor Adjunto\n'
                              ' 3.Assistente\n'
                              'Opção: '))
                while cat<1 or cat>3:
                    cat=int(input('Opção Inválida! Opção: '))
            except ValueError:
                print('Não foi inserido um número.')
        if cat==1:
            cat='Professor'
        elif cat==2:
            cat='Professor Adjunto'
        elif cat==3:
            cat='Assistente'
        for objeto in self.__Professores:
            categ=objeto.GETcategoria()
            if cat==categ:
                objeto.PROFshow()
                cont+=1
        if cont==0:
            print('Não foi encontrado nenhum Professor nessa categoria.')

    def SEARCHcc(self):
        cc=-1
        cont=0
        while cc<0:
            try:
                cc=int(input('Indique o CC pelo qual procura: '))
                while cc<0:
                    cc=int(input('CC Inválido! CC: '))
            except ValueError:
                print('Não foi inserido um número.')
        for i in self.__Alunos:
            geter=i.GETCC()
            if geter==cc:
                i.ALshow()
                cont+=1
        for i in self.__Professores:
            geter=i.GETCC()
            if geter==cc:
                i.ALshow()
                cont+=1
        if cont==0:
            print('Não foi encontrado ninguém com esse CC.')

    def getAlunosLista(self):
        return self.__Alunos

    def getProfLista(self):
        return self.__Professores

class Pessoa:

    def __init__(self,CC,NIF):
        self.__CC=CC
        self.__NIF=NIF

    def PESSshow(self):
        print('CC: %d' %self.__CC)
        print('NIF: %d' %self.__NIF)

    def GETCC(self):
        return self.__CC

    def GETNIF(self):
        return self.__NIF

class Aluno(Pessoa):
    def __init__(self,CC,NIF,NumMec,Curso,Ano):
        super().__init__(self,CC,NIF)
        self.__NumMec=NumMec
        self.__Curso=Curso
        self.__Ano=Ano

    def ALUshow(self):
        super().PESSshow()
        print('Numero Mecanografico: %d' %self.__NumMec)
        print('Curso: %s' %self.__Curso)
        print('Ano: %d' %self.__Ano)

    def getNumMec(self):
        return self.__NumMec

class Professor(Pessoa):
    def __init__(self,CC,NIF,NumFunc,Departamento,Categoria,Habilitacoes):
        super().__init__(self,CC,NIF)
        self.__NumFunc=NumFunc
        self.__Departamento=Departamento
        self.__Categoria=Categoria
        self.__Habilitacoes=Habilitacoes

    def PROFshow(self):
        super().PESSshow()
        print('Numero de Funcionário: %d' %self.__NumFunc)
        print('Departamento: %s' %self.__Departamento)
        print('Categoria: %s' %self.__Categoria)
        print('Habilitações: %s' %self.__Habilitacoes)

    def GETcategoria(self):
        return self.__Categoria

    def GETNumFunc(self):
        return self.__NumFunc

def inserir():
    esact=EsACT()
    print('-'*80)
    opc=-1
    while opc<0:
        try:
            opc=int(input('1.Aluno\n'
                          '2.Professor\n'
                          'Opção'))
            while opc<1 or opc>2:
                opc=int(input('Opção Inválida!\nOpção:'))
        except ValueError:
            print('Não foi inserido um número!')
    contador=0
    while contador==0:
        contador=0
        if opc==1:
            print('-'*80)
            CC=-1
            while CC<0:
                try:
                    CC=int(input('CC: '))
                    while CC<0:
                        CC=int(input('CC Inválido! CC: '))
                except ValueError:
                    print('Não foi inserido um número!')
            NIF=-1
            while NIF<0:
                try:
                    NIF=int(input('NIF: '))
                    while NIF<0:
                        NIF=int(input('NIF Inválido! NIF: '))
                except ValueError:
                    print('Não foi inserido um número!')
            NumMec=-1
            while NumMec<0:
                try:
                    NumMec=int(input('Numero Mecanográfico: '))
                    while NumMec<0:
                        NumMec=int(input('Número Inválido! Numero Mecanográfico: '))
                except ValueError:
                    print('Não foi inserido um número!')
            Curso=-1
            while Curso<0:
                try:
                    Curso=int(input('Curso:\n'
                                    '   1.Comunicação e Jornalismo\n'
                                    '   2.Design de Jogos Digitais\n'
                                    '   3.Gestão e Admnistração Pública\n'
                                    '   4.Informática e Comunicações\n'
                                    '   5.Marketing\n'
                                    '   6.Multimédia\n'
                                    '   7.Solicitadoria\n'
                                    '   8.Turismo\n'
                                    'Opção: '))
                    while Curso<1 or Curso>8:
                        Curso=int(input('Opção Inválida! Opção:'))
                except ValueError:
                    print('Não foi inserido um número!')
            Ano=-1
            while Ano<0:
                try:
                    Ano=int(input('Ano: '))
                    while Ano<1 or Ano>3:
                        Ano=int(input('Ano Inválido! Ano: '))
                except ValueError:
                    print('Não foi inserido um número!')
            if Curso==1:
                Curso='Comunicação e Jornalismo'
            elif Curso==2:
                Curso='Design de Jogos Digitais'
            elif Curso==3:
                Curso='Gestão e Admnistração Pública'
            elif Curso==4:
                Curso='Informática e Comunicações'
            elif Curso==5:
                Curso='Marketing'
            elif Curso==6:
                Curso='Multimédia'
            elif Curso==7:
                Curso='Solicitadoria'
            elif Curso==8:
                Curso='Turismo'
            lista=esact.getAlunosLista()
            cont=0
            for i in lista:
                if i.getNumMec==NumMec or i.GETCC==CC or i.GETNIF==NIF:
                    cont+=1
            if cont==0:
                contador=1
                esact.ADDaluno(CC,NIF,NumMec,Curso,Ano) #!!!
            elif cont>0:
                contador=0
                print('Aluno já inserido!')
        elif opc==2:
            print('-'*80)
            CC=-1
            while CC<0:
                try:
                    CC=int(input('CC: '))
                    while CC<0:
                        CC=int(input('CC Inválido! CC: '))
                except ValueError:
                    print('Não foi inserido um número!')
            NIF=-1
            while NIF<0:
                try:
                    NIF=int(input('NIF: '))
                    while NIF<0:
                        NIF=int(input('NIF Inválido! NIF: '))
                except ValueError:
                    print('Não foi inserido um número!')
            NumFunc=-1
            while NumFunc<0:
                try:
                    NumFunc=int(input('Numero de Funcionário: '))
                    while NumFunc<0:
                        NumFunc=int(input('Numero Inválido! Numero de Funcionário: '))
                except ValueError:
                    print('Não foi inserido um número!')
            Departamento=str(input('Departamento: '))
            Categoria=-1
            while Categoria<0:
                try:
                    Categoria=int(input('Categoria:\n'
                                        '   1.Professor\n'
                                        '   2.Professor Adjunto\n'
                                        '   3.Assistente\n'
                                        'Opção: '))
                    while Categoria<1 or Categoria>3:
                        Categoria=int(input('Opção Inválida! Opção: '))
                except ValueError:
                    print('Não foi inserido um numero.')
            if Categoria==1:
                Categoria='Professor'
            elif Categoria==2:
                Categoria='Professor Adjunto'
            elif Categoria==3:
                Categoria='Assistente'
            Habilitacoes=-1
            while Habilitacoes<0:
                try:
                    Habilitacoes=int(input('Habilitações:\n'
                                           '    1.Mestrado\n'
                                           '    2.Doutoramento\n'
                                           'Opção: '))
                    while Habilitacoes<1 or Habilitacoes>2:
                        Habilitacoes=str(input('Opção Inválida! Habilitações: '))
                except ValueError:
                    print('Não foi inserido um número')
            if Habilitacoes==1:
                Habilitacoes='Mestrado'
            elif Habilitacoes==2:
                Habilitacoes='Doutoramento'
            lista=esact.getProfLista()
            cont=0
            for e in lista:
                if e.GETCC==CC or e.GETNIF==NIF or e.GETNumFunc==NumFunc:
                    cont+=1
            if cont==0:
                esact.ADDprofessor(CC,NIF,NumFunc,Departamento,Categoria,Habilitacoes)
                contador=1
            elif cont>0:
                contador=0


def menu():
    esact=EsACT()
    opco=-1
    print('-'*80)
    while opco<0:
        try:
            opco=int(input('Indique a opção que quer:\n'
                           '    1.Inserir\n'
                           '    2.Mostrar\n'
                           '    3.Pesquisar Aluno por Número Mec\n'
                           '    4.Pesquisar Professor por Categoria\n'
                           '    5.Pesquisar CC\n'
                           '    6.Terminar\n'
                           'Opção: '))
            while opco<1 or opco>6:
                opco=int(input('Opção Inválida! Opção: '))
        except ValueError:
            print('Não foi inserido um número.')
    if opco==1:
        inserir()
        menu()
    elif opco==2:
        esact.showAlProf()
        menu()
    elif opco==3:
        esact.searchALUNOnumMec()
        menu()
    elif opco==4:
        esact.searchPROFcat()
        menu()
    elif opco==5:
        esact.SEARCHcc()
        menu()
    elif opco==6:
        print('Programa Terminado')
        pass

menu()