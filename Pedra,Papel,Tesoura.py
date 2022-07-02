import random
player1 = str(input('Digite o seu nome: '))
print("Escolha uma opção")
print('''[0] Pedra
[1] Papel
[2] Tesoura''')
game = ['Pedra', 'Papel', 'Tesoura']
opc = int(input('Digite a sua opçao: '))
if opc >= 3 or opc < 0:
    print("Digite um número válido!")
computer_choice = random.randint(0, 2)
print(f'O jogador {player1} escolheu:')
print(f'{game[opc]}')
print('Computador escolheu: ')
print(f'{game[computer_choice]}')
if opc == 0 and computer_choice == 2:
    print(f'O jogador {player1} venceu')
elif opc == 1 and computer_choice  == 0:
    print(f'O jogador {player1} venceu')
elif opc == 2 and computer_choice == 1:
    print(f'O jogador {player1} venceu')
elif opc == computer_choice:
    print("Deu empate :/")
else:
    print("O computador venceu.")