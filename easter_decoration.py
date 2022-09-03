
number_of_customers = int(input())
command = input()
number_of_baskets = 0
number_of_wreath = 0
number_of_chocolate_bunny = 0
price_for_all_baskets = 1.5 * number_of_baskets
price_for_all_wreath = 3.8 * number_of_wreath
price_for_all_chocolate_bunny = 7 * number_of_chocolate_bunny
total_quantity = number_of_chocolate_bunny + number_of_wreath + number_of_baskets
total_price = price_for_all_baskets + price_for_all_wreath + price_for_all_chocolate_bunny

for x in range(number_of_customers):
    while command != 'Finish':

        if command == 'basket':
            number_of_baskets += 1

        elif command == 'wreath':
            number_of_wreath += 1
        elif command == 'chocolate bunny':
            number_of_chocolate_bunny += 1
        command = input()

    if total_quantity % 2 == 0:
        total_price *= 0.80
        print(f'You purchased {total_quantity} item for {total_price} leva.')
    else:
        print(f'You purchased {total_quantity} item for {total_price} leva.')


avg_bill = total_price / number_of_customers
print(f'Average bill per client is: {avg_bill:.2f} leva.')
