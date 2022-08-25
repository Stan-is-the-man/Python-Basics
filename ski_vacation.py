days_for_the_trip = int(input())
type_of_accommodation = input()
feedback = input()

nights_for_the_trip = days_for_the_trip - 1
room_price_per_night = 18.00
apartment_price_per_night = 25.00
president_apart_per_night = 35.00
final_price = 0

if type_of_accommodation == 'room for one person':
    final_price = nights_for_the_trip * room_price_per_night
elif type_of_accommodation == 'apartment':
    if days_for_the_trip < 10:
        final_price = nights_for_the_trip * apartment_price_per_night * 0.70
    elif 10 <= days_for_the_trip <= 15:
        final_price = nights_for_the_trip * apartment_price_per_night * 0.65
    else:
        final_price = nights_for_the_trip * apartment_price_per_night * 0.50
elif type_of_accommodation == 'president apartment':
    if days_for_the_trip < 10:
        final_price = nights_for_the_trip * president_apart_per_night * 0.90
    elif 10 <= days_for_the_trip <= 15:
        final_price = nights_for_the_trip * president_apart_per_night * 0.85
    else:
        final_price = nights_for_the_trip * president_apart_per_night * 0.80

if feedback == 'positive':
    final_price *= 1.25
else:
    final_price *= 0.90

print(f'{final_price:.2f}')