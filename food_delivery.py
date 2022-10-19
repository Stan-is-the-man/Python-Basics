qt_chicken = int(input())
qt_fish = int(input())
qt_veggie = int(input())

price_chicken = qt_chicken * 10.35
price_fish = qt_fish * 12.4
price_veggie = qt_veggie * 8.15

sum_of_all_dishes = price_veggie + price_fish + price_chicken
price_desert = 0.2 * sum_of_all_dishes


total_price = sum_of_all_dishes + price_desert + 2.5


print(round(total_price , 2))



