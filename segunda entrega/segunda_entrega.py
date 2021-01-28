import random 
#atributos do lutador
nomeMT=["Bruno","Pedro","Pedro","Pedro","Pedro","Thiago","João","José","Antônio","Francisco","Carlos","Matheus","Paulo","Lucas","Luiz","Gabriel","Daniel","Marcelo","Eduardo","Felipe","Rodrigo","Sócrates","Arthur","Lorenzo","Théo","Pedro Henrique","Gustavo","Murilo","Vitor","João Vitor"]
nomeFT=["Diana","Mariana","Cecíla","Camila","Fernanda","Antônia","Ana","Ana Maria","Cláudia","Ana Cláudia","Maria","Beatriz","Laura","Emanuela","Mel","Jéssica","Júlia","Isabela","Luísa","Heloísa","Sofia","Laura","Alice","Gabriela","Maria Eduarda"]
nomeST=["Dias","Porto","Silva","da Silva","Santos","Oliveira","Souza","Costa","Ferreira","Barbosa","Amaral","Soares","Alves","Andrade","Castro","Carvalho","Lima","Gomes","Costa","Ribeiro"]
#faixasjh=["roxa","marrom","preta"]
#faixasjf=["azul","roxa","marrom","preta"]
#faixasm1=["amarelo","verde","azul"]
#faixasm2=["marrom","vermelha"]
faixasK=["verde","roxa","marrom","preta"]

#atributos do torneio
nomeTT=["Torneio do Vale","Campeonato da Costa","Prova do Alto","Primeiro Campeonato da Confederação Brasileira","Competição Nacional","Torneio Local"]
pesoTT={"L":"Leve","M":"Médio","P":"Pesado","S":"Super pesado"}
sexoTT={"M":"Masculino","F":"Feminino"}
tipoTT={"T":"Todos contra todos","MM":"Mata-mata"}
categoriaTT={
    "1":"Junior Laranja",
    "2":"Junior Vermelha",
    "3":"Junior Livre",
    "4":"Sub-21 Verde",
    "5":"Sub-21 Roxa",
    "6":"Sub-21 Marrom",
    "7":"Sub-21 Livre",
    "8":"Senior Preta 1° Dan",
    "9":"Senior Preta 2° Dan",
    "10":"Senior Livre"}
pesoTTR={"L":range(51,60),"M":range(61,70),"P":range(71,80),"SP":range(81,100)}
idadeTTR={"JUN":[14,15,16,17],"SEN":[18,19,20],"SEN":range(21,35)}
categoriaTTR={}
faixaTT={"1":"Laranja","2":"Vermelha","4":"Verde","5":"Roxa","6":"Marrom","8":"Preta 1° Dan","9":"Preta 2° Dan"}


class Torneio: #ok
    nomeE=random.choice(nomeTT)+" de Karatê"
    tipoE=random.randint(list(tipoTT.keys()))           #T ou MM
    sexoE=random.randint(list(sexoTT.keys()))           #M ou F
    pesoE=random.choice(list(pesoTT.keys()))            #L, M, P ou SP | [51,60], [61,70], [71,80] ou [81,100]
    categoriaE=random.choice(list(categoriaTT.keys()))  #JUN(1,2,3), S21(4,5,6,7) ou SEN(8,9,10) | [14,17], [18,20] ou [21,35]
    def __init__(self,sexoE,pesoE,categoriaE,tipoE):
        self.sexoE=sexoE           
        self.categoriaE=categoriaE 
        self.nomeE=nomeE            
        self.pesoE=pesoE                 

def criarTorneio(): #ok
    while True:
        sexoI=input("\t\tM=Masculino\n\t\tF=Femenino\n\tEscreva o sexo dos lutadores do torneio: ")
        if sexoI!="M" or sexoI!="F":
            print("\tSexo inválido para o torneio!\n")
        else:
            print("\n")
            break
    while True:
        pesoI=input("\t\tL=Leve\n\t\tM=Médio\n\t\tP=Pesado\n\t\tSP=Super pesado\n\tEscreva o peso dos lutadores do torneio: ")
        if list(pesoTT.keys()).count(pesoI)==1:
            print("\n")
            break
        else:
            print("\tPeso inválido para o torneio!\n")
    while True:
        categoriaI=input("\t\t1=Junior Laranja\n\t\t2=Junior Vermelho\n\t\t3=Junior Livre\n\t\t4=Sub-21 Verde\n\t\t5=Sub-21 Roxa\n\t\t6=Sub-21 Marrom\n\t\t7=Sub-21 Livre\n\t\t8=Senior Preta 1° Dan\n\t\t9=Senior Preta 2° Dan\n\t\t10=Senior Livre\n\tEscreva a caterogia do torneio: ")
        try:
            categoriaI=int(categoriaI)
        except ValueError:
            print("\tCategoria inválida para o torneio!\n")
        if categoriaI in range(1,10):
            break
        elif isinstance(categoriaI,int):
            print("\tCategoria inválida para o torneio!\n")
    while True:
        tipoI=input("\t\tT=Todos contra todos (pontuação)\n\t\tMM=Mata-mata\n\tEscreva o tipo de torneio: ")
        if tipoI=="T" or tipoI=="MM":
            print("\n")
            break
        else:
            print("\tTipo inválido para o torneio!\n")
    return sexoI, pesoI, categoriaI, tipoI

class Lutador: #ok
    amarcial="Karateca"
    def __init__(self,nome,nomeS,sexo,idade,peso,altura,categoria,treino,sorte): #nomeI,nomeSI,sexoI,idadeI,pesoI,alturaI
        self.sexo=sexo                 #(M,F) segundo sexoE
        self.categoria=categoria       #[1,10] segundo categoriaE
        self.nome=nome                 #determinado noutra função segundo sexoE
        self.nomeS=nomeS               #sobrenome
        self.idade=idade               #[14,15,16,17], [18,19,20] ou [21,35]
        self.treino=treino             #[50,95]
        self.sorte=sorte               #[0,5]
        if                             #determinada noutra função segundo faixaTT
        self.faixa=faixaTT[categoria]  
        self.peso=peso                 #[51,60], [61,70], [71,80] ou [81,100] segundo pesoTT?
        self.altura=altura             #[1.60,2.10]
    
def inscreverLutador(): #quase, quase lá
    while True:
        nomeI,nomeSI=input("\tEscreva o nome completo do lutador: ",sep=" ")
        if nomeI=="" or nomeI==" " or nomeSI=="" or nomeSI==" ":
            print("\tNome inválido para o lutador!\n")
        else: 
            print("\n")
            break
    while True:                                                          #pode ser otimizado sabendo sexoE, nem precisa ser incluido na verdade
        sexoI=input("\tEscreva o sexo do lutador (M/F): ")
        if sexoI!="M" or sexoI!="F":
            print("\tSexo inválido para o lutador!\n")
        else:
            print("\n")
            break
    while True:                                                          #consertado
        idadeI=input("\tEscreva a idade inteira do lutador: ")
        try:
            idadeI=int(idadeI)
        except ValueError:
            print("\tIdade inválida para o lutador!\n")
        if range(14,17).count(idadeI)==1 and range(1,3).count(torneioE.tipoE)==1:
            print("\n")
            break
        elif range(18,20).count(idadeI)==1 and range(4,7).count(torneioE.tipoE)==1:
            print("\n")
            break
        elif range(21,35).count(idadeI)==1 and range(8,10).count(torneioE.tipoE)==1:
            print("\n")
            break
        elif isinstance(idadeI,int):
            print("\tIdade inválida para o lutador!\n")
    while True:                                                          #consertado, acho
        pesoI=input("\tEscreva o peso inteiro em kilogramas do lutador: ")
        try:
            pesoI=int(pesoI)
        except ValueError:
            print("\tPeso inválido para o lutador!\n")
        if range(51,60).count(pesoI)==1 and torneioE.pesoE=="L":
            print("\n")
            break
        elif range(61,70).count(pesoI)==1 and torneioE.pesoE=="M":
            print("\n")
            break
        elif range(71,80).count(pesoI)==1 and torneioE.pesoE=="P":
            print("\n")
            break
        elif range(81,100).count(pesoI)==1 and torneioE.pesoE=="SP":
            print("\n")
            break
        elif isinstance(pesoI,int):
            print("\tIdade inválida para o lutador!\n")
    while True:
        alturaI=input("\tEscreva a altura em metros do lutador: ")
        try:
            alturaI=round(float(alturaI),2)
        except ValueError:
            print("\tAltura inválida para o lutador!\n")
        if alturaI<=1.60 or alturaI>=2.10:
            print("\tAltura muito baixa ou muito alta para o lutador!\n")
        else:
            print("\n")
            break
    categoriaI=torneioE.categoriaE()
    
    return nomeI,nomeSI,sexoI,idadeI,pesoI,alturaI

torneioE=Torneio()

def gerarLutador(sexoL,categoriaL,pesoL): #?????
    sexoL=torneioE.sexoE
    if sexoL="H":
        nomeL=random.choice(nomeMT)
    else:
        nomeL=random.choice(nomeFT)
    nomeSL=random.choice(nomeST)
    if torneio
    if torneioE.pesoE=="L":
        pesoL=random.randint(51,60)
    elif torneioE.pesoE=="M":
        pesoL=random.randint(61,70)
    elif torneioE.pesoE=="P":
        pesoL=random.randint(71,80)
    elif torneioE.pesoE=="SP":
        pesoL=random.randint(81,100)

lutadores=[Lutador() for i in range(8)]
loc=0
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
        torneioE=Torneio()
    elif loc=="e":
        print("\tAté mais!\n")
        break
    else:
        print("\tEscolha inválida!\n")
"""
while loc!="e": 
    loc=input("Escolha uma opção:\ne) Encerrar\n2) Criar torneio\n3) Torneio aleatório\n\t")
    if loc=="2":
        while loc!="e" or loc!="4":
            loc=input("Configure o torneio:\ne) Encerrar\n4) Voltar ao menu principal\n5) Inscrever lutador\n6) Tipo de torneio\n7) Categoria\n8) Simular uma luta\n9) Simular Torneio\n\t")
            if loc=="5":
                #nome e sobrenome do lutador
                #altura
                #peso
                #registrar em class
            elif loc=="6":
                while loc!="e" or loc!="4" or loc!="10":
                    loc=input("Configure o torneio:\ne) Encerrar\n4) Voltar ao menu principal\n10) Voltar ao menu de torneios\n11) Todos contra todos\n12) Mata-mata\n\t")
                    if loc=="11":
                        #torneio todos contra todos
                    elif loc=="12":
                        #torneio mata-mata
                    else: print("\tEscolha inválida!\n")
            elif loc=="7":
                 while loc!="e" or loc!="4" or loc!="10":
                    loc=input("Configure o torneio:\ne) Encerrar\n4) Voltar ao menu principal\n10) Voltar ao menu de torneios\n13) Sexo\n14) Peso\n15) Idade\n\t")
                    if loc=="13":
                        #masculino ou feminino
                    elif loc=="14":
                        #pena, leve, médio, pesado ou super pesado
                    elif loc=="15":
                        #jovem, sub-21 e sensei
                    else: print("\tEscolha inválida!\n")
            elif loc=="8":
                #escolher oponente while if loop
                #resultado
            elif loc=="9":
                #simular torneio
                #imprimir ranking
            elif loc=="4": print("\tRetorno ao menu principal.\n")
            else: print("\tEscolha inválida!\n")
    elif loc=="3": print("\tSimulando torneio...\n")
        #simular torneio
        #imprimir ranking
    elif loc=="e": print("\tAté mais!\n")
    else: print("\tEscolha inválida!\n")
"""