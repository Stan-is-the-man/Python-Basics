import sys
command = input()
max_goals = -sys.maxsize

while command != 'END':
    number_of_goals = int(input())
    if number_of_goals > max_goals:
        max_goals = number_of_goals
        best_player = command
    if number_of_goals >= 10:
        break
    command = input()

print(f'{best_player} is the best player!')
if max_goals >= 3:
    print(f'He has scored {max_goals} goals and made a hat-trick !!!')
else:
    print(f'He has scored {max_goals} goals.')

