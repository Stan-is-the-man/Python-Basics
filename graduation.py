name = input()

sum_of_scores = 0
class_year = 1
bad_grade = 0
avg_score = 0

while class_year <= 12 and bad_grade != 2:
    scores = float(input())

    if scores >= 4:
        sum_of_scores += float(scores)
        class_year += 1
    else:
        bad_grade += 1


if bad_grade == 2:
    print(f'{name} has been excluded at {class_year} grade ')
else:
    avg_score = sum_of_scores / 12
    print(f'{name} graduated. Average grade: {avg_score:.2f}')