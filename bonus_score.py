number = int(input())
# first IF
if number <= 100:
    bonus_points = 5

elif 100 < number <= 1000:
    bonus_points = number * 0.2

else:
    bonus_points = number * 0.1

# second IF - независим от първия
# promenlivata bonus_points si se pishe navsqkuade s tova ime

if number % 2 == 0: # ако е четно
    bonus_points = bonus_points + 1     # това може да се напише и bonus_points += 1

# third if
if number % 10 == 5: # ако завършва на 5
    bonus_points += 2


print(bonus_points)
total_number = number + bonus_points
print(total_number)


