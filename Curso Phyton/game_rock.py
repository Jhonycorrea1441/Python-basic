import random

def play():
    user = input("What´s your choise? 'R' for Rock, 'P' for paper, 'S' for scissors... ")
    computer = random.choice(['R','P','S'])

    if user == computer:
        return 'It/´s a tie'
    
    # R>S, S>P, P>R

    if is_win(user, computer):
        return 'You Won!'

    return 'You Lost!'

def is_win(player, opponent):
    # Return true if player wins.
    # R>S, S>P, P>R
    if (player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
        return True
    

print(play())