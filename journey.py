budget = float(input())
season = input()

type_of_vacation = ''
destination = ''
price_for_accomodation = ''

if season == 'summer':
    type_of_vacation = 'Camp'
elif season == 'winter':
    type_of_vacation = 'Hotel'

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price_for_accomodation = budget * 0.3
    elif season == 'winter':
        price_for_accomodation = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price_for_accomodation = budget * 0.4
    elif season == 'winter':
        price_for_accomodation = budget * 0.8
elif budget > 1000:
    destination = 'Europe'
    type_of_vacation = "Hotel"
    price_for_accomodation = budget * 0.9


print(f'Somewhere in {destination}')
print(f'{type_of_vacation} - {price_for_accomodation:.2f}')






