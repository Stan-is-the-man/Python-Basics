number_of_eggs_first_player = int(input())
number_of_eggs_second_player = int(input())
command = ''
while command != 'End of battle':
    command = input()
    if command == 'one':
        number_of_eggs_second_player -= 1
        if number_of_eggs_second_player == 0:
            print(f'Player two is out of eggs. Player one has {number_of_eggs_first_player} eggs left.')
            break

    elif command == 'two':
        number_of_eggs_first_player -= 1
        if number_of_eggs_first_player == 0:
            print(f'Player one is out of eggs. Player two has {number_of_eggs_second_player} eggs left.')
            break
if command == "End of battle":
    print(f'Player one has {number_of_eggs_first_player} eggs left.')
    print(f'Player two has {number_of_eggs_second_player} eggs left.')
