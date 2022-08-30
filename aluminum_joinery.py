number_of_windows = int(input())
type_of_windows = input()
type_of_delivery = input()

delivery = 0
windows_price = 0
if number_of_windows < 10:
    print('Invalid order')


if type_of_delivery == 'With delivery':
    delivery = 60

if type_of_windows == '90X130':

    if 30 < number_of_windows <= 60:
        windows_price = 110 * 0.95
    elif number_of_windows > 60:
        windows_price = 110 * 0.92
    else:
        windows_price = 110

if type_of_windows == '100X150':

    if 40 < number_of_windows <= 80:
        windows_price = 140 * 0.94
    elif number_of_windows > 80:
        windows_price = 140 * 0.90
    else:
        windows_price = 140
if type_of_windows == '200X300':

    if 25 < number_of_windows <= 50:
        windows_price = 250 * 0.91
    elif number_of_windows > 50:
        windows_price = 250 * 0.86
    else:
        windows_price = 250
if type_of_windows == '130X180':

    if 20 < number_of_windows <= 50:
        windows_price = 190 * 0.93
    elif number_of_windows > 50:
        windows_price = 190 * 0.88
    else:
        windows_price = 190

price_of_windows = number_of_windows * windows_price
if number_of_windows > 99 and number_of_windows > 10 :
    total = (price_of_windows + delivery) * 0.96
else:
    total = price_of_windows + delivery

if number_of_windows > 10:
    print(f'{total:.2f} BGN')
