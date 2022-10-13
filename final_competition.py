number_of_dancers = int(input())
points = float(input())
season = input()
place = input()

prize_money = 0

if place == 'Bulgaria':
    prize_money = points * number_of_dancers
elif place == 'Abroad':
    prize_money = (number_of_dancers * points) + (number_of_dancers * points * 0.5)

if season == 'summer':
    if place == 'Bulgaria':
        prize_money *= 0.95
    elif place == 'Abroad':
        prize_money *= 0.90
elif season == 'winter':
    if place == 'Bulgaria':
        prize_money *= 0.92
    elif place == 'Abroad':
        prize_money *= 0.85

without_charity = prize_money * 0.25
charity = prize_money * 0.75
prize_per_dancer = without_charity / number_of_dancers

print(f'Charity - {charity:.2f}')
print(f'Money per dancer - {prize_per_dancer:.2f}')
