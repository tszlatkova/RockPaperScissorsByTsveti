import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'

print("During the game, the result will be displayed as follow -> player's wins : draws : computer's wins. ")
player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')

game = 0
player_wins = 0
computer_wins = 0
draws = 0

while player_move != 'e':

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print('Invalid Input. Try again...')
        player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')
        continue

    game += 1
    computer_random_number = random.randint(1, 3)

    computer_move = ''

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f'The computer chose {computer_move}.')

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_wins += 1
    elif player_move == computer_move:
        draws += 1
    else:
        computer_wins += 1

    print(f'The result for game {game} is: {player_wins}:{draws}:{computer_wins}.\n')

    player_move = input('Choose [r]ock, [p]aper, [s]cissors or [e]nd: ')

print()

if player_wins > computer_wins:
    print('End of the game! You won!')
    print()
    # printing a heart
    for row in range(0, 6):
        for col in range(0, 7):
            if (row == 0 and col % 3 != 0) or (row == 1 and col % 3 == 0) or (row - col == 2) or (row + col == 8):
                print('*', end=' ')
            else:
                print(' ', end=' ')
        print()  # to start the next row on new line

elif player_wins < computer_wins:
    print('End of the game! Sorry, but the computer won!')
else:
    print('End of the game! No one wins!')
