dog_food = int(input())
command = input()

total_eaten_food = 0
dog_food_in_grams = dog_food * 1000

while command != 'Adopted':
    eaten_food = int(command)
    total_eaten_food += eaten_food
    command = input()

diff = abs(total_eaten_food - dog_food_in_grams)

if total_eaten_food > dog_food_in_grams:
    print(f'Food is not enough. You need {diff} grams more.')
else:
    print(f'Food is enough! Leftovers: {diff} grams.')