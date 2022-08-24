budget = int(input())
season = input()
fishermen_count = int(input())

boat_rent = 0

if season == "Spring":
    boat_rent = 3000
elif season == 'Summer' or season == 'Autumn':
    boat_rent = 4200
elif season == 'Winter':
    boat_rent = 2600


if fishermen_count <= 6:
    boat_rent *= 0.9
elif fishermen_count <= 11:
    boat_rent *= 0.85
else:
    boat_rent *= 0.75

if (fishermen_count % 2 == 0) and (season != 'Autumn'):
    boat_rent *= 0.95

diff = abs(budget - boat_rent)

if budget >= boat_rent:
    print(f'Yes! You have {diff:.2f} leva left.')
else:
    print(f'Not enough money! You need {diff:.2f} leva.')
