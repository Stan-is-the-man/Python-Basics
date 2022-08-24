month = input()
number_of_nights = int(input())

price_for_apartment = 0
price_for_studio = 0

if month == 'May' or month == 'October':
    if 7 < number_of_nights <= 14:
        price_for_studio = number_of_nights * 50 * 0.95
        price_for_apartment = 65 * number_of_nights
    elif number_of_nights > 14:
        price_for_studio = number_of_nights * 50 * 0.70
        price_for_apartment = 65 * number_of_nights * 0.9
    else:
        price_for_apartment = 65 * number_of_nights
        price_for_studio = 50 * number_of_nights
elif month == 'June' or month == 'September':
    if number_of_nights > 14:
        price_for_studio = 75.20 * number_of_nights * 0.8
        price_for_apartment = 68.70 * number_of_nights * 0.9
    else:
        price_for_apartment = 68.70 * number_of_nights
        price_for_studio = 75.20 * number_of_nights
elif month == 'July' or month == 'August':
    if number_of_nights > 14:
        price_for_studio = 76 * number_of_nights
        price_for_apartment = 77 * number_of_nights * 0.9
    else:
        price_for_studio = 76 * number_of_nights
        price_for_apartment = 77 * number_of_nights

print(f"Apartment: {price_for_apartment:.2f} lv.")
print(f'Studio: {price_for_studio:.2f} lv.')
