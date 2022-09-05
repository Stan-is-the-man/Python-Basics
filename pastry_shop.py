type_of_cake = input()
number_of_cakes = int(input())
day_of_december = int(input())
cake_price = 0
if type_of_cake == 'Cake':
    if day_of_december <= 15:
        cake_price = number_of_cakes * 24
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75
        cake_price *= 0.90

    elif day_of_december > 15:
        cake_price = number_of_cakes * 28.70
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75
elif type_of_cake == 'Souffle':
    if day_of_december <= 15:
        cake_price = number_of_cakes * 6.66
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75
        cake_price *= 0.90
    elif day_of_december > 15:
        cake_price = number_of_cakes * 9.8
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75

else:
    if day_of_december <= 15:
        cake_price = number_of_cakes * 12.6
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75
        cake_price *= 0.90

    elif day_of_december > 15:
        cake_price = number_of_cakes * 16.98
        if 100 <= cake_price <= 200 and day_of_december <= 22:
            cake_price *= 0.85
        elif cake_price > 200:
            cake_price *= 0.75


print(f'{cake_price:.2f}')
