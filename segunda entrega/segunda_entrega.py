import random 
#atributos do lutador
nomeMasculinoTodos=["Bruno","Pedro","Pedro","Pedro","Pedro","Thiago","João","José","Antônio","Francisco","Carlos","Matheus","Paulo","Lucas","Luiz","Gabriel","Daniel","Marcelo","Eduardo","Felipe","Rodrigo","Sócrates","Arthur","Lorenzo","Théo","Pedro Henrique","Gustavo","Murilo","Vitor","João Vitor"]
nomeFemeninoTodos=["Diana","Mariana","Cecíla","Camila","Fernanda","Antônia","Ana","Ana Maria","Cláudia","Ana Cláudia","Maria","Beatriz","Laura","Emanuela","Mel","Jéssica","Júlia","Isabela","Luísa","Heloísa","Sofia","Laura","Alice","Gabriela","Maria Eduarda"]
sobrenomeTodos=["Dias","Porto","Silva","da Silva","Santos","Oliveira","Souza","Costa","Ferreira","Barbosa","Amaral","Soares","Alves","Andrade","Castro","Carvalho","Lima","Gomes","Costa","Ribeiro"]

#atributos do torneio
#relação categoria-idade e categoria-faixa são para gerar os outros lutadores
nomeTorneioTodos=["Torneio do Vale","Campeonato da Costa","Prova do Alto","Primeiro Campeonato da Confederação Brasileira","Competição Nacional","Torneio Local"]
sexoTorneiosTodos={"M":"Masculino","F":"Feminino"}
pesoTorneiosTodos={"L":range(51,61),"M":range(61,71),"P":range(71,81),"SP":range(81,101)}
categoriaTorneiosTodos={
    "1":"Junior Laranja","2":"Junior Vermelha","3":"Junior Livre",
    "4":"Sub-21 Verde","5":"Sub-21 Roxa","6":"Sub-21 Marrom","7":"Sub-21 Livre",
    "8":"Senior Preta 1° Dan","9":"Senior Preta 2° Dan","10":"Senior Livre"}
categoriaIdadeTorneios={
    "1":range(14,18),"2":range(14,18),"3":range(14,18),
    "4":range(18,21),"5":range(18,21),"6":range(18,21),"7":range(18,21),
    "8":range(21,36),"9":range(21,36),"10":range(21,36)}
categoriaFaixaTorneios={
    "1":["Laranja"],"2":["Vermelha"],"3":["Laranja","Vermelha"],
    "4":["Verde"],"5":["Roxa"],"6":["Marrom"],"7":["Verde","Roxa","Marrom"],
    "8":["Preta 1° Dan"],"9":["Preta 2° Dan"],"10":["Preta 1° Dan"¨,"Preta 2° Dan"]}
tipoTorneiosTodos={"T":"Todos contra todos","MM":"Mata-mata"}


class Torneio: #classe determina por default uma configuração de torneio usando chaves
    nomeEscolhido=random.choice(nomeTorneiosTodos)+" de Karatê"            #Nome
    sexoEscolhido=random.choice(list(sexoTorneiosTodos.keys()))            #Masculino ou Feminino
    pesoEscolhido=random.choice(list(pesoTorneiosTodos.keys()))            #Leve, Médio, Pesado ou Super pesado 
    categoriaEscolhido=random.choice(list(categoriaTorneiosTodos.keys()))  #Junior, Sub-21 ou Senior
    tipoEscolhido=random.randint(list(tipoTorneiosTodos.keys()))           #Todos contra todos ou Mata-mata 
    def __init__(self,sexoEscolhido,pesoEscolhido,categoriaEscolhido,tipoEscolhido): #configuração manual
        self.sexoEscolhido=sexoEscolhido   
        self.pesoEscolhido=pesoEscolhido           
        self.categoriaEscolhido=categoriaEscolhido 
        self.tipoEscolhido=tipoEscolhido            

def criarTorneio(): #função retorna atributos da class Torneio pelo método __init__() 
    while True:
        sexoDeterminado=input("\t\tM=Masculino\n\t\tF=Femenino\n\tEscreva o sexo dos lutadores do torneio: ")
        if sexoDeterminado!="M" or sexoDeterminado!="F":
            print("\tSexo inválido para o torneio!\n")
        else:
            print("\n")
            break
    while True:
        pesoInscrição=input("\t\tL=Leve\n\t\tM=Médio\n\t\tP=Pesado\n\t\tSP=Super pesado\n\tEscreva o peso dos lutadores do torneio: ")
        if list(pesoTorneiosTodos.keys()).count(pesoDeterminado)==1:
            print("\n")
            break
        else:
            print("\tPeso inválido para o torneio!\n")
    while True:
        categoriaDeterminado=input("\t\t1=Junior Laranja\n\t\t2=Junior Vermelho\n\t\t3=Junior Livre\n\t\t4=Sub-21 Verde\n\t\t5=Sub-21 Roxa\n\t\t6=Sub-21 Marrom\n\t\t7=Sub-21 Livre\n\t\t8=Senior Preta 1° Dan\n\t\t9=Senior Preta 2° Dan\n\t\t10=Senior Livre\n\tEscreva a caterogia do torneio: ")
        try:
            categoriaDeterminado=int(categoriDeterminadoo)
        except ValueError:
            print("\tCategoria inválida para o torneio!\n")
        if categoriaDeterminado in range(1,11):
            break
        elif isinstance(categoriaDeterminado,int):
            print("\tCategoria inválida para o torneio!\n")
    while True:
        tipoDeterminado=input("\t\T=Todos contra todos (pontuação)\n\t\tMM=Mata-mata\n\tEscreva o tipo de torneio: ")
        if tipoInscrição=="T" or tipoInscrição=="MM":
            print("\n")
            break
        else:
            print("\Tipo inválido para o torneio!\n")
    return sexoDeterminado, pesoDeterminado, categoriaDeterminado, tipoDeterminado

class Lutador(object): #class lutador para gerar e inscrever lutadores, apenas usa o método  __init__()
    def __init__(self,nome,sobrenome, sexo,peso,categoria,idade,faixa,altura,número): 
        #atributo do número do lutador
        self.número=número
        #atributos irrelevantes
        self.nome=nome
        self.sobrenome=sobrenome   
        #atributos de torneio                     
        self.categoria=categoria     
        #atributos controláveis mas limitados
        self.sexo=sexo
        self.peso=peso     
        self.idade=idade               
        self.faixa=faixa
         self.altura=altura
        #atributos únicos e aleatórios
        self.treino=random.randint(range(50,96))     
        self.sorte=random.randint(range(0,6))                 

def inscreverLutador(sexoEscolhido,pesoEscolhido,categoriaEscolhido): #determina os atributos dum lutador pelo usuário
    while True:
        nomeCompletoInscrição=input("\tEscreva o nome completo do lutador: ")
        nomeInscrição=nomeCompletoInscrição.split()[0]
        sobrenomeInscrição=nomeCompletoInscrição.split()[-1]
        if nomeInscrição==sobrenomeInscrição:
            print("\tNome inválido para o lutador!\n")
        else: 
            print("\n")
            break
    while True: #compara o input do sexo com aquele definido no torneio, sexoEscolhido
        sexoInscrição=input("\tEscreva o sexo do lutador (M/F): ")
        if sexoInscrição!=sexoEscolhido:
            print("\tSexo inválido para o lutador!\n")
        else:
            print("\n")
            break
    while True: #compara o input da idade com aquela permitida no torneio, pesoEscolhido
        idadeInscrição=input("\tEscreva a idade inteira do lutador: ")
        if categoriaIdadeTorneios[categoriaEscolhido].count(idadeInscrição)==1:
            print("\n")
            break
        else:
            print("\tIdade inválida para o lutador!\n")
    while True: #compara o input do peso com aquele definido no torneio, pesoEscolhido
        pesoInscrição=input("\tEscreva o peso inteiro em kilogramas do lutador: ")
        if pesoTorneiosTodos[pesoEscolhido].count(pesoInscrição)==1:
            print("\n")
            break
        else:
            print("\tPeso inválido para o lutador!\n")
    while True: #compara o input da faixa com aquela definida no torneio, categoriaEscolhida
        faixaInscrição=input("\tEscreva a faixa com maiúscula do lutador: ")
        if categoriafaixaTorneios[categoriaEscolhido].count(faixaInscrição)==1:
            print("\n")
            break
        else:
            print("\tFaixa inválida para o lutador!\n")
    while True:
        alturaInscrição=input("\tEscreva a altura em metros do lutador (0.00): ")
        try:
            alturaInscrição=round(float(alturaInscrição),2)
        except ValueError:
            print("\tAltura inválida para o lutador!\n")
        if alturaInscrição<1.60:
            print("\tAltura muito baixa para o lutador!\n")
        elif alturaInscrição>2.10:
            print("\tAltura muito alta para o lutador!\n")
        else:
            print("\n")
            break
    categoriaInscrição=torneioEscolhido.categoriaEscolhido
    return nomeInscrição,sobrenomeInscrição,sexoInscrição,pesoInscrição,categoriaInscrição,idadeInscrição,faixaInscrição,alturaInscrição

def gerarLutador(sexoEscolhido,pesoEscolhido,categoriaEscolhido): #determina os atributos dum lutador aleatoriamente
    sexoSorteado=torneioEscolhido.sexoEscolhido
    if sexoSorteado=="H":
        nomeSorteado=random.choice(nomeMasculinoTodos)
    else:
        nomeSorteado=random.choice(nomeFemeninoTodos)
    sobrenomeSorteado=random.choice(sobrenomeTodos)
    pesoSorteado=random.randint(pesoTorneiosTodos[pesoEscolhido])
    categoriaSorteado=categoriaEscolhido
    idadeSorteado=random.randint(categoriaIdadeTorneios[categoriaEscolhido])
    faixaSorteado=random.choice(categoriaFaixaTorneios[categoriaEscolhido])
    alturaSorteado=round(random.uniform(1.60,2.10),2)
    return nomeSorteado,sobrenomeSorteado,sexoSorteado,pesoSorteado,categoriaSorteado,idadeSorteado,faixaSorteado,alturaSorteado

def luta(altura1,peso1,treino1,sorte1,altura2,peso2,treino2,sorte2):
    desição=round(((treino1+sorte1-1)/(treino2+sorte2-1))^3+(altura1^2*peso1)/(altura2^2*peso2),3)
    if desição>1.000:
        return 1,0
    else:
        return 0,1
def torneioT(vitórias,altura1,peso1,treino1,sorte1,altura2,peso2,treino2,sorte2):
    
#dispocições iniciais do programa
torneioE=Torneio
lutadores=[]
vitórias=[0,0,0,0,0,0,0,0]
for i in range(8):
    lutadores.append(Lutador(i))
loc=0
#menu da entrega
while True:
    loc=input("Escolha uma opção:\n1) Torneio definido\n2) Torneio aleatório\ne) Encerrar\n\t")
    if loc=="1":
        while True:
            torneioE=Torneio(self,criarTorneio())
            loc=input("Escolha uma opção:\n1) Inscrever lutador\n2) Ver lutadores\n3) Simular Luta\n4) Simular torneio\nv) Voltar\n\t")
            if loc=="1":
                lutadores.append(lutador.(self,inscreverLutador(),torneioE.categoriaE,)
            elif loc=="2":
                for n in range(8):
                    
            elif loc=="3":

            elif loc=="4":
                if TorneioE.tipoE()="T"
                
                else:

            elif loc=="v":
                print("\n")
                break
        if loc=="1":
    elif loc=="2":
        print("\tSimulando torneio...\n")
        
    elif loc=="e":
        print("\tAté mais!\n")
        break
    else:
        print("\tEscolha inválida!\n")
