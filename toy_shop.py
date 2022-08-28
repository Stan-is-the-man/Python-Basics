price_trip = float(input())

qt_puzzles = int(input())
qt_dolls = int(input())
qt_bears = int(input())
qt_minions = int(input())
qt_trucks = int(input())

qt_all_toys = qt_trucks + qt_minions + qt_bears + qt_dolls + qt_puzzles


puzzles_price = 2.6
doll_price = 3
bear_price = 4.1
minion_price = 8.2
truck_price = 2

total_puzzles = qt_puzzles * puzzles_price
total_dolls = qt_dolls * doll_price
total_bears = qt_bears * bear_price
total_minions = qt_minions * minion_price
total_trucks = qt_trucks * truck_price

total_price_all_toys = total_trucks + total_bears + total_dolls + total_minions + total_puzzles

if qt_all_toys >= 50:
    total_price_all_toys *= 0.75

rent = total_price_all_toys * 0.1

profit_total = total_price_all_toys - rent

difference = abs(profit_total - price_trip)


if profit_total >= price_trip:
    print(f"Yes! {difference:.2f} lv left.")
elif profit_total < price_trip:
    print(f"Not enough money! {difference:.2f} lv needed.")





