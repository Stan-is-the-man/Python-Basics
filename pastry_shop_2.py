type_of_cake = input()
number_of_cakes = int(input())
day_of_december = int(input())
cake_price = 0
if type_of_cake == 'Cake':
    if 1 <= day_of_december <= 15:
        cake_price = number_of_cakes * 24
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75
    elif 15 < day_of_december <= 24:
        cake_price = number_of_cakes * 28.70
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75
elif type_of_cake == 'Souffle':
    if 1 <= day_of_december <= 15:
        cake_price = number_of_cakes * 6.66
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75

    elif 15 < day_of_december <= 24:
        cake_price = number_of_cakes * 9.8
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75

elif type_of_cake == 'Baklava':
    if 1 <= day_of_december <= 15:
        cake_price = number_of_cakes * 12.6
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75
    elif 15 < day_of_december <= 24:
        cake_price = number_of_cakes * 16.98
        if day_of_december <= 22:
            if 100 <= cake_price <= 200:
                cake_price *= 0.85
            elif cake_price > 200:
                cake_price *= 0.75

if day_of_december <= 15:
    print(f'{0.9 * cake_price:.2f}')
else:
    print(f'{cake_price:.2f}')
