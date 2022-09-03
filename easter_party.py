number_of_guests = int(input())
price_for_kuvert_for_one_person = float(input())
budget = float(input())

price_cake = 0.1 * budget

if 10 <= number_of_guests <= 15:
    price_for_kuvert_for_one_person *= 0.85
elif 15 < number_of_guests <= 20:
    price_for_kuvert_for_one_person *= 0.80
elif number_of_guests > 20:
    price_for_kuvert_for_one_person *= 0.75

all_costs = price_cake + (number_of_guests * price_for_kuvert_for_one_person)
diff = abs(budget - all_costs)

if all_costs <= budget:
    print(f'It is party time! {diff:.2f} leva left.')
else:
    print(f'No party! {diff:.2f} leva needed.')