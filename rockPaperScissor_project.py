import random
user_choice = int(input('Enter your choice for the game ,rock:0,paper:1,scissor:2 :'))
if user_choice >=3 or user_choice < 0:
    print('you entered wrong value, you lose...')
else:
    computer_choice = random.randint(0,2)
    print('computer_choice:')
    print(computer_choice)
    if computer_choice == user_choice:
        print('Game is Draw')
    elif user_choice == 0 and computer_choice == 2:
        print('you win')
    elif computer_choice == 0 and user_choice == 2:
        print('you lose...')
    elif user_choice > computer_choice:
        print('you win')
    elif computer_choice > user_choice:
        print('you lose')
    