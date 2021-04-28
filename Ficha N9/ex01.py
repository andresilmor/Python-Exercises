#Sabendo que a EsACT agrega docentes e alunos, em que os docentes são caraterizados
#por: número de funcionário, nome, categoria (e.g. assistente, professor adjunto),
#departamento e habilitações (e.g. Mestrado, doutoramento); e que os alunos são
#caraterizados por: número mecanográfico, nome, curso e ano.
#   a. Crie as classes EsACT, Docente e Aluno.
#   b. Implemente os construtores nas respetivas classes que considere adequados
#      para que possam ser criados objetos.
#   c. Implemente na classe EsACT os seguintes métodos (defina os parâmetros que
#      considere adequados para os métodos solicitados) bem como todos os
#      métodos de suporte que sejam necessários:
#       i. inserirDocente
#       ii. inserirAluno
#       iii. pesquisarDocente (por número de funcionário)
#       iv. pesquisarDocente (por departamento)
#       v. listarAlunosPorCurso
#       vi. removerAluno (por número mecanográfico)
#   d. Se fosse criada uma nova classe Curso, que alterações, em seu entender,
#      deveriam ser efetuadas, na estrutura da sua implementação?       ?_?

class EsACT:

    def __init__(self):
        self.Aluno=None
        self.Docente=None

class Docente:

    def __init__(self,NumFunc,Nome,Categoria,Departamento,Habilitacoes):
        self.__NumFunc=NumFunc
        self.__Nome=Nome
        self.__Categoria=Categoria
        self.__Departamento=Departamento
        self.__Habilitacoes=Habilitacoes

    def getNumFunc(self):
        return self.__NumFunc

    def getDepartamento(self):
        return self.__Departamento

    def DOCshow(self):
        print('Número de Funcionário: %s' %self.__NumFunc)
        print('Nome: %s' %self.__Nome)
        print('Categoria: %s' %self.__Categoria)
        print('Departamento: %s' %self.__Departamento)
        print('Habilitações: %s' %self.__Habilitacoes)

class Aluno:
    def __init__(self,NumMec,Nome,Curso,Ano):
        self.__NumMec=NumMec
        self.__Nome=Nome
        self.__Curso=Curso
        self.__Ano=Ano

    def getCurso(self):
        return self.__Curso

    def ALUNOshow(self):
        print('Número Mecanográfico: %d' %self.__NumMec)
        print('Nome: %s' %self.__Nome)
        print('Curso: %s' %self.__Curso)
        print('Ano: %s' %self.__Ano)

    def getNumMec(self):
        return self.__NumMec

def menu():
    opc=str(input('Indique qual opção quer:\n'
                  'A.Inserir Docente\n'
                  'B.Inserir Aluno\n'
                  'C.Pesquisar Docente por Departamento\n'
                  'D.Pesquisar Docente por Número de Funcionário\n'
                  'E.Listar Alunos por curso\n'
                  'F.Remover Aluno\n'
                  'G.Terminar Programa\n'
                  'Opção: '))
    while opc not in 'AaBbCcDdEeFf':
        opc=str(input('Opção Inválida!\nOpção: '))
    return opc

def insALUNO():
    try:
        NumMec=int(input('Numero Mecanográfico: '))
        while NumMec<0:
            NumMec=int(input('Número Inválido!\nNumero Mecanográfico: '))
    except ValueError:
        print('Não foi inserido um número.')
    Nome=str(input('Nome: '))
    Curso=str(input('Curso: '))
    while Curso.upper() != ('MULTIMEDIA' or 'MARKETING' or 'TURISMO' or 'DJD'): #Esqueci me dos outros kkk
        Curso=str(input('Curso Inválido!\nCurso: '))
    try:
        Ano=int(input('Ano: '))
        while Ano<0:
            Ano=int(input('Ano Inválido!\nAno:'))
    except ValueError:
        print('Não foi inserido um número.')
    aluno=Aluno(NumMec,Nome,Curso,Ano)
    print('-'*80)
    return aluno

def insDOCENTE():
    try:
        NumFunc=int(input('Numero de Funcionário: '))
        while NumFunc<0:
            NumFunc=int(input('Numero Inválido!\nNumero de Funcionário: '))
    except ValueError:
        print('Não foi inserido um número.')
    Nome=str(input('Nome: '))
    Categoria=str(input('Categoria: '))
    while Categoria.upper() != ('ASSISTENTE' or 'PROFESSOR ADJUNTO' or 'PROFESSOR'):
        Categoria=str(input('Categoria Inválida!\nCategoria: '))
    Departamento=str(input('Departamento: '))
    Habilitacoes=str(input('Habilitações: '))
    while Habilitacoes.upper() != ('MESTRADO' or 'DOUTORAMENTO'):
        Habilitacoes=str(input('Habilitação Inválida!\nHabilitações: '))
    docente=Docente(NumFunc,Nome,Categoria,Departamento,Habilitacoes)
    print('-'*80)
    return docente

def DOCENTEsearchDEP(lista):
    sear=str(input('Indique o departamento do funcionário que procura: '))
    cont=False
    for i in lista:
        dep=i.getDepartamento()
        if sear==dep:
            i.DOCshow()
            cont=True
    if cont==False:
        print('Não foi encontrado nenhum funcionário nesse departamento.')

def DOCENTEsearchNUM(lista):
    cont=False
    try:
        sear=int(input('Indique o número do funcionário que procura: '))
        while sear<0:
            sear=int(input('Número Inválido!\nIndique o número do funcionário que procura: '))
    except ValueError:
        print('Não foi inserido um número.')
    for i in lista:
        num=i.getNumFunc()
        if sear==num:
            i.DOCshow()
            cont=True
    if cont==False:
        print('Não foi encontrado nenhum funcionário com esse número.')
    print('-'*80)

def LISTARcurso(lista):
    print('Lista de Alunos: ')
    mul=mar=tur=djd=0
    print('Multimédia: ')
    for a in lista:
        cur=a.getCurso()
        if cur.upper()=='MULTIMEDIA':
            a.ALUNOshow()
            print(' '*80)
            mul+=1
    if mul==0:
        print('Não foi encontrado nenhum aluno de Multimédia.\n')
    print('Marketing: ')
    for b in lista:
        cur=b.getCurso()
        if cur.upper()=='MARKETING':
            b.ALUNOshow()
            print(' '*80)
            mar+=1
    if mar==0:
        print('Não foi encontrado nenhum aluno de Marketing.\n')
    print('Turismo: ')
    for c in lista:
        cur=c.getCurso()
        if cur.upper()=='TURISMO':
            c.ALUNOshow()
            print(' '*80)
            tur+=1
    if tur==0:
        print('Não foi encontrado nenhum aluno de Turismo.\n')
    print('DJD (Design de Jogos Digitais): ')
    for d in lista:
        cur=d.getCurso()
        if cur.upper()=='DJD':
            d.ALUNOshow()
            print(' '*80)
            djd+=1
    if djd==0:
        print('Não foi encontrado nenhum aluno de DJD.\n')

    def DELaluno(self,lista):
        try:
            num=int(input('Indique o número mecanográfico do aluno que quer remover: '))
            while num<0:
                num=int(input('Número Inválido!\nIndique o número mecanográfico: '))
        except ValueError:
            print('Não foi inserido um número.')
        for i in lista:
            mec=i.getNumMec()
            if mec==num:
                del lista[i]
        return lista

def DELaluno(lista):
    try:
        num=int(input('Indique o número mecanográfico do aluno que quer remover: '))
        while num<0:
            num=int(input('Número Inválido!\nIndique o número mecanográfico: '))
    except ValueError:
        print('Não foi inserido um número.')
    for i in lista:
        mec=i.getNumMec()
        if mec==num:
            del lista[i]
    return lista

listaAl=[]
listaDoc=[]
opc=menu()
cont=True
while cont==True:
    if opc in 'Aa':
        doc=insDOCENTE()
        listaDoc.append(doc)
        opc=menu()
    elif opc in 'Bb':
        doc=insALUNO()
        listaAl.append(doc)
        opc=menu()
    elif opc in 'Cc':
        DOCENTEsearchDEP(listaDoc)
        opc=menu()
    elif opc in 'Dd':
        DOCENTEsearchNUM(listaDoc)
        opc=menu()
    elif opc in 'Ee':
        LISTARcurso(listaAl)
        opc=menu()
    elif opc in 'Ff':
        listaAl=DELaluno(listaAl)
        opc=menu()
    elif opc in 'Gg':
        cont=False
print('Programa Terminado')


