number_of_computers = int(input())
number_of_sales = 0
total_score_points = 0
for x in range(number_of_computers):
    number = int(input())
    score = number % 10
    estimated_sales = number // 10
    if score == 2:
        real_sales = 0 * estimated_sales
        number_of_sales += real_sales
        total_score_points += score
    elif score == 3:
        real_sales = 0.5 * estimated_sales
        number_of_sales += real_sales
        total_score_points += score
    elif score == 4:
        real_sales = 0.7 * estimated_sales
        number_of_sales += real_sales
        total_score_points += score
    elif score == 5:
        real_sales = 0.85 * estimated_sales
        number_of_sales += real_sales
        total_score_points += score
    elif score == 6:
        real_sales = estimated_sales
        number_of_sales += real_sales
        total_score_points += score
avg_score = total_score_points / number_of_computers
print(f'{number_of_sales:.2f}')
print(f'{avg_score:.2f}')




