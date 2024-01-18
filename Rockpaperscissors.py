import random

moves = ['rock', 'paper', 'scissors']
player_score = 0
computer_score = 0
total_moves = 10

for _ in range(total_moves):
    player_move = input("Choose your move: ")
    player_move = player_move.lower()

    if player_move not in moves:
        print("Invalid move! Please choose from rock, paper, or scissors.")
        continue

    computer_move = random.choice(moves)
    print("Computer chose:", computer_move)

    if player_move == computer_move:
        print("It's a tie!")
    elif (player_move == 'rock' and computer_move == 'scissors') or \
        (player_move == 'paper' and computer_move == 'rock') or \
        (player_move == 'scissors' and computer_move == 'paper'):
        player_score += 1
        print("Player Won!")
    else:
        computer_score += 1
        print("Computer Won!")

    print("Player Score:", player_score)
    print("Computer Score:", computer_score)
    print("Moves Left:", total_moves - (_ + 1))
    print()

if player_score > computer_score:
    print("Player Won the Game!")
elif player_score < computer_score:
    print("Computer Won the Game!")
else:
    print("It's a Tie!")