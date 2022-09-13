from math import floor

number_of_tournaments = int(input())
initial_points = int(input())

won_points = 0
won_tournaments = 0

for x in range(number_of_tournaments):
    phaze_of_tournament = input()
    if phaze_of_tournament == 'W':
        won_points += 2000
        won_tournaments += 1
    elif phaze_of_tournament == 'F':
        won_points += 1200
    elif phaze_of_tournament == 'SF':
        won_points += 720

final_points = won_points + initial_points
average_points = won_points / number_of_tournaments
won_tournaments_percent = (won_tournaments / number_of_tournaments) * 100

print(f'Final points: {final_points}')
print(f'Average points: {floor(average_points)}')
print(f'{won_tournaments_percent:.2f}%')
