import random

user_wins = 0
computer_wins = 0

options = ['p', 'r', 's']

while True:
    user_input = input('type p for "paper", r for "rock", s for "scissors" or q to quit: ').lower()
    if user_input == 'q':
        print('thanks for playing...')
        break
        
    if user_input not in options:
        print('invalid input, try again...')
        continue

    random_num = random.randint(0, 2)
    computer_pick = options[random_num]
    print(f'computer picked {computer_pick}')

    if user_input == computer_pick:
        print('it is a tie!')
        continue
    elif user_input == 'p' and computer_pick == 'r':
        print('you win!')
        user_wins += 1
    elif user_input == 'r' and computer_pick == 's':
        print('you win!')
        user_wins += 1
    elif user_input == 's' and computer_pick == 'p':
        print('you win!')
        user_wins += 1
    else:
        print('computer wins!')  
        computer_wins += 1

print(f'you won {user_wins} times and computer won {computer_wins} times')

if user_wins > computer_wins:
    print('you won more than computer, congratulations!')
elif computer_wins > user_wins:
    print('computer won more than you, better luck next time!')
else:
    print('it is a tie! you and computer won the same amount of times!')


print('Goodbye...')