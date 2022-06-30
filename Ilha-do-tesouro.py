from time import sleep
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a ilha do tesouro.")
print("Seu objetivo é encontrar o tesouro.")
print("Você está no meio de uma floresta em uma ilha deserta, na sua frente possui duas placas: ")
print("Uma direcionando para esquerda e a outra para direita")
sleep(2)
print("A placa da esquerda tem escrito: CUIDADO!")
print("A placa da direita tem escrito: PERIGO!")
sleep(1)
print("Qual placa caminho voce decide seguir ? (Direita/Esquerda)")
resposta = str(input("Qual é a sua resposta ? ")).lower()
sleep(1)
print("Andando...")
sleep(1)
if resposta == "esquerda":
    print("Voce entrou pelo caminho da esquerda")
    sleep(1)
    print("Durante o caminho você encontra uma ponte velha com algumas tábuas soltas e abaixo dela tem um riacho")
    print("Voce deseja atravessar a ponte por cima ou pelo riacho ? ")
    print('''[1] Passar por cima da ponte
[2] Passar por baixo da ponte(pelo riacho)''')
    resposta2 = int(input("Digite a sua opcao: "))
    if resposta2 == 1:
        print("Voce decidiu passar por cima da ponte velha, porém algumas tábuas estavam soltas e durante a passagem"
              "voce acabou sofrendo um acidente, pois uma tábua quebrou e fez voce cair da ponte")
        sleep(1)
        print('Voce falhou')
    elif resposta2 == 2:
        print("Voce atravessou a ponte por baixo e acabou evitando o perigo de se machucar na ponte, após atravessar "
              "a ponte, voce chega em uma área aberta da ilha")
        print("Na área aberta, voce encontra uma pá e logo mais na frente um X acima de um monte de areia fofa")
        sleep(1)
        print("Voce deseja pegar a pá ? ")
        print('''[1] Sim
[2] Nao''')
        resposta3 = int(input("Digite a sua opcao: "))
        if resposta3 == 1:
            print("Voce pegou a pá e conseguiu encontrar o tesouro ! ")
            print("Voce venceu :)")
        else:
            print("Voce não pegou a pá e não encontrou o tesouro")
            print("Voce falhou :(")
elif resposta == "direita":
    print("Voce entrou pelo caminho da direita")
    print("Infelizmente ao entrar pelo caminho da direita, voce se deparou com varias cobras venenos"
          " e acabou sendo picado")
    print("Voce falhou :(")