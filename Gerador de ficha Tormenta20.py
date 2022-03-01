from random import randint

mod_Forca = mod_Destreza = mod_Constituicao = mod_Inteligencia = mod_Sabedoria = mod_Carisma = 0
Atr = {"For": [0,mod_Forca],"Des": [0,mod_Destreza],"Con": [0,mod_Constituicao],
       "Int": [0,mod_Inteligencia],"Sab": [0,mod_Sabedoria],"Car": [0,mod_Carisma]}
Vetor_rolagem = [0]*4
Vetor_pericias_base = ["Atletismo", "Luta", "Acrobacia", "Cavalgar", "Furtividade", "Iniciativa",
                       "Ladinagem", "Pilotagem", "Pontaria", "Fortitude", "Conhecimento", "Cura",
                       "Guerra", "Investigação", "Misticismo", "Nobreza", "Ofício", "Intuição",
                       "Percepção", "Reflexos", "Religião", "Sobrevivência", "Vontade" "Adestramento",
                       "Atuação", "Diplomacia", "Enganação", "Intimidação", "Jogatina"]
#O vetor de perícias está organizado de acordo com o tipo de atributo relacionado a tais perícias,
#na mesma ordem padrão: Força(1ª a 4ª), Destreza(5ª ao 9ª), Constituição(10ª), Inteligência(11ª a 17ª),
#Sabedoria(18ª a 23ª) e Carisma(24ª a 29ª). NOTA: Depois explicarei o porquê de não usar um dicionário.
Pericias_treinadas = {}
Pericias_ntreinadas = {}
Pericias_jogador = [Pericias_treinadas,Pericias_ntreinadas]
EspCar = []
NumPoder = [0]

#INÍCIO DO PROGRAMA
#Coleta de dados:
Raca = input("Escolha sua raça!: ")
Nivel = int(input("Nível: "))
Rolar_Atributo = int(input("\nVocê já rolou seus atributos?\n1-Sim       2-Não \n: "))
if Rolar_Atributo == 1:
    for i in Atr:
        Atr[i][0] = int(input("Preencha: %s " % i))
else:
    retorno = 1
    while retorno !=0:
        for i in Atr:
            for j in range(0,4):
                Vetor_rolagem[j] = randint(1,6)
            Atr[i][0] = sum(Vetor_rolagem) - min(Vetor_rolagem)
            valor = Atr[i][0]
            print("%s : %d" % (i, Atr[i][0]))
        op1 = int(input("\nDeseja rolar os dados novamente?\n1-Sim      2-Não\n:"))
        if op1 == 1:
            pass
        elif op1 == 2:
            retorno = 0
        else:
            print("Opção inválida")






#Primeiro devemos calcular os atributos e definir as características especiais
#do personagem, baseados na raça (e subraça se houver).
def CalcRaca(Raca, Atr, EspCar, NumPoder,Pericias_treinadas, Pericias_ntreinadas, retorno ):
    if Raca == "Humano":
        #ATRIBUTOS:
        AtrEsc1 = input("\nEscolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ")
        AtrEsc2 = input(("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ", ""))
        AtrEsc3 = input((("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ", "")) \
                        .replace(" " + AtrEsc2 + " ", ""))
        if AtrEsc1 in [AtrEsc2,AtrEsc3] or AtrEsc2 == [AtrEsc1,AtrEsc3]:
            print("\nHumanos não podem escolher atributos iguais, pressione ENTER para refazer")
            return 0
        elif AtrEsc1 in Atr and AtrEsc2 in Atr and AtrEsc3 in Atr:
            Atr[AtrEsc1][0] += 2
            Atr[AtrEsc2][0] += 2
            Atr[AtrEsc3][0] += 2
        else:
            print("Atributo inválido, pressione ENTER para refazer")
            input()
            return 0
        #CARACTERÍSTICAS
        esp1 = int(input("\nVERSÁTIL: Você se torna treinado em duas perícias a sua escolha \n"
              "(não precisam ser da sua classe). Você pode trocar uma dessas \n"
              "perícias por um poder geral a sua escolha. \n"
              "Deseja trocar uma perícia treinada por um poder geral?\n"
              "1-sim        2-não\n"
              ": "))
        if not esp1 in [1,2]:
            print("Opção inválida, pressione ENTER para refazer")
            input()
            return 0
        cont0 = soma = 0
        if esp1 == 1:
            NumPoder[0] += 1
            cont0 += 1
        while cont0 != 2:
            esp2 = int(input("\nOk! Escolha sua(s) perícia(s) treinada(s): \n"
"\n"
"   FORÇA:         DESTREZA:        CONSTITUIÇÃO:      INTELIGÊNCIA:         SABEDORIA:        CARISMA:         \n"
"1-Atletismo     5-Furtividade     10- Fortitude      11-Conhecimento       18-Intuição       24-Adestramento   \n"
"2-Luta          6-Iniciativa                         12-Cura               19-Percepção      25-Atuação        \n"
"3-Acrobacia     7-Ladinagem                          13-Guerra             20-Reflexos       26-Diplomacia     \n"
"4-Cavalgar      8-Pilotagem                          14-Investigação       21-Religião       27-Enganação      \n"
"                9-Pontaria                           15-Misticismo         22-Sobrevivência  28-Intimidação    \n"
"                                                     16-Nobreza            23-Vontade        29-Jogatina       \n"
"                                                     17-Ofício                                                 \n"
                             ": "))
            soma += esp2
            if (soma - esp2) == esp2:
                print("\nVocê já escolheu essa perícia, pressione ENTER para refazer")
                input()
                return 0
            else:
                cont0 += 1
                Pericias_treinadas[Vetor_pericias_base[esp2-1]] = 0
                retorno[0] = 0
    elif Raca == "1":
        #ATRIBUTOS:
        Atr["Destreza"][0] -= 2
        Atr["Constituição"][0] += 4
        Atr["Sabedoria"][0] += 2
        #CARACTERÍSTICAS:
        EspCar.apend("Visão no escuro")
    elif Raca == "Dahllan":
        Atr["Destreza"][0] += 2
        Atr["Inteligência"][0] -= - 2
        Atr["Sabedoria"][0] += 4
    elif Raca == "Elfo":
        Atr["Destreza"][0] += 2
        Atr["Constituição"][0] -= 2
        Atr["Inteligência"][0] += 4
    elif Raca == "Goblin":
        Atr["Destreza"][0] += 4
        Atr["Inteligência"][0] += 2
        Atr["Carisma"][0] -= 2
    elif Raca == "Lefou":
        AtrEsc1 = input("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  ")
        AtrEsc2 = input(("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  ").replace(" " + AtrEsc1 + " ", ""))
        AtrEsc3 = input((("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  ").replace(" " + AtrEsc1 + " ", "")) \
                        .replace(" " + AtrEsc2 + " ", ""))
        if "Car" in [AtrEsc1,AtrEsc2,AtrEsc3]:
            print("Lefous não podem escolher CARISMA, aperte ENTER para refazer.")
            input()
            return 0
        elif AtrEsc1 in [AtrEsc2,AtrEsc3] or AtrEsc2 == [AtrEsc1,AtrEsc3]:
            print("Lefous não podem escolher atributos iguais, aperte ENTER para refazer.")
            input()
            return 0
        elif AtrEsc1 in Atr and AtrEsc2 in Atr and AtrEsc3 in Atr:
            Atr[AtrEsc1][0] += 2
            Atr[AtrEsc2][0] += 2
            Atr[AtrEsc3][0] += 2
            Atr["Carisma"][0] -= 2
        else:
            print("Atributo inválido")
    elif Raca == "Minotauro":
        Atr["Força"][0] += 4
        Atr["Constituição"][0] += 2
        Atr["Sabedoria"][0] -= 2
    elif Raca == "Qareen":
        Atr["Carisma"][0] += 4
        Atr["Inteligência"][0] += 2
        Atr["Sabedoria"][0] -= 2
    elif Raca == "Golem":
        Atr["Força"][0] += 4
        Atr["Constituição"][0] += 2
        Atr["Carisma"][0] -= 2
    elif Raca in ["Hynne","Halflings"]:
        Atr["Destreza"][0] += 4
        Atr["Carisma"][0] += 2
        Atr["Força"][0] -= 2
    elif Raca == "Kliren":
        Atr["Inteligência"][0] += 4
        Atr["Carisma"][0] += 2
        Atr["Força"][0] -= 2
    elif Raca == "Medusa":
        Atr["Destreza"][0] += 4
        Atr["Carisma"][0] += 2
    elif Raca == "Osteon":
        AtrEsc1 = input("Escolha adicionar 2 pontos a:  For  Des  Int  Sab  Car  " )
        AtrEsc2 = input(("Escolha adicionar 2 pontos a:  For  Des  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ",""))
        AtrEsc3 = input((("Escolha adicionar 2 pontos a:  For  Des  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ", ""))\
    .replace(" " + AtrEsc2 + " ",""))
        if "Con" in [AtrEsc1,AtrEsc2, AtrEsc3]:
            print("Osteons não podem escolher CONSTITUIÇÃO, pressione ENTER para refazer.")
            input()
            return 0
        elif AtrEsc1 in [AtrEsc2,AtrEsc3] or AtrEsc2 == [AtrEsc1,AtrEsc3]:
            print("Osteons não podem escolher atributos iguais, pressione ENTER para refazer.")
            input()
            return 0
        elif AtrEsc1 in Atr and AtrEsc2 in Atr and AtrEsc3 in Atr:
            Atr[AtrEsc1][0] += 2
            Atr[AtrEsc2][0] += 2
            Atr[AtrEsc3][0] += 2
            Atr["Constituição"][0] -= 2
        else:
            print("Atributo inválido, pressione ENTER para refazer.")
            input()
            return 0
    elif Raca in ["Sereia","Tritão"]:
        AtrEsc1 = input("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ")
        AtrEsc2 = input(("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ", ""))
        AtrEsc3 = input((("Escolha adicionar 2 pontos a:  For  Des  Con  Int  Sab  Car  ").replace(" " + AtrEsc1 + " ", "")) \
                        .replace(" " + AtrEsc2 + " ", ""))
        if AtrEsc1 in [AtrEsc2, AtrEsc3] or AtrEsc2 == [AtrEsc1, AtrEsc3]:
            print("Sereias/Tritões não podem escolher atributos iguais, pressione ENTER para refazer.")
            input()
            return 0
        elif AtrEsc1 in Atr and AtrEsc2 in Atr and AtrEsc3 in Atr:
            Atr[AtrEsc1][0] += 2
            Atr[AtrEsc2][0] += 2
            Atr[AtrEsc3][0] += 2
        else:
            print("Atributo inválido, pressione ENTER para refazer")
            input()
            return 0
    elif Raca == "Sílfide":
        Atr["Carisma"][0] += 4
        Atr["Destreza"][0] += 2
        Atr["Força"][0] -= 4
    elif Raca == "Suraggel":
        Subr = input("Escolha sua subraça, Aggelus (celestiais) ou Sulfure (abismais): ")
        if Subr == "Sulfure":
            Atr["Destreza"][0] += 4
            Atr["Inteligência"][0] += 2
        elif Subr == "Aggelus":
            Atr["Sabedoria"][0] += 4
            Atr["Carisma"][0] += 2
        else:
            print("Subraça inválida, pressione ENTER para refazer")
            input()
            return 0
    elif Raca == "Trog":
        Atr["Constituição"][0] += 4
        Atr["Força"][0] += 2
        Atr["Inteligência"][0] -= 2

retorno = [1]
while retorno[0] != 0:
    CalcRaca(Raca, Atr, EspCar, NumPoder, Pericias_treinadas, Pericias_ntreinadas, retorno)


#Exibição para testes:
#RAÇA:
print("Raça: ", Raca)

#ATRIBUTOS:
print("\n--------------------------------------------------------------------------------------------------------------------------"
      "\nSeus atributos:")
for i in Atr:
    print("%s : %d" % (i, Atr[i][0]))

#CARACTERÍSTICAS RACIAIS:
print("\n--------------------------------------------------------------------------------------------------------------------------"
      "\nCaracterísticas especiais")
for j in range(0,len(EspCar)):
    print(EspCar[j])

#PERICIAS
print("\n--------------------------------------------------------------------------------------------------------------------------"
      "\nPerícias:")
for k in Pericias_ntreinadas:
    print("%s: %s" % (k, Pericias_ntreinadas[k]))

print("\nPerícias TREINADAS")
for l in Pericias_treinadas:
    print("%s: %s" % (l, Pericias_treinadas[l]))
#PODERES
print("\n--------------------------------------------------------------------------------------------------------------------------"
      "\nPoderes a escolher: ", NumPoder[0])






