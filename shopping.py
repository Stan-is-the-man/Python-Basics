budget = float(input())
qt_of_video_cards = int(input())
qt_processors = int(input())
qt_ram = int(input())

price_video_card = 250

all_video_cards = qt_of_video_cards * price_video_card
price_processor = 0.35 * all_video_cards * qt_processors
price_ram = 0.1 * all_video_cards * qt_ram

total = all_video_cards + price_processor + price_ram

if qt_of_video_cards > qt_processors:
    total *= 0.85

diference = abs(total - budget)

if budget >= total:
    print(f"You have {diference:.2f} leva left!")

if budget < total:
    print(f"Not enough money! You need {diference:.2f} leva more!")



