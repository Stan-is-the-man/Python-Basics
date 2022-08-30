
n = int(input())
points = 0
red_points = 0
orange_points = 0
yellow_points = 0
white_points = 0
black_points = 0
other_points = 0
for number in range(n):
    color = input()
    if color == 'red':
        points += 5
        red_points += 1
    elif color == 'orange':
        points += 10
        orange_points += 1
    elif color == 'yellow':
        points += 15
        yellow_points += 1
    elif color == 'white':
        points += 20
        white_points += 1
    elif color == 'black':
        points //= 2
        black_points += 1
    else:
        other_points += 1

print(f'Total points: {points}')
print(f'Points from red balls: {red_points}')
print(f'Points from orange balls: {orange_points}')
print(f'Points from yellow balls: {yellow_points}')
print(f'Points from white balls: {white_points}')
print(f'Other colors picked: {other_points}')
print(f'Divides from black balls: {black_points}')