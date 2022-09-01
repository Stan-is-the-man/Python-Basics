percent_fat = int(input())
percent_proteins = int(input())
percent_carb = int(input())
total_calories = int(input())
percent_water = int(input())

grams_from_fat = ((percent_fat / 100) * total_calories) / 9

grams_from_proteins = ((percent_proteins / 100) * total_calories) / 4
grams_from_carb = ((percent_carb / 100) * total_calories) / 4

food_grams = grams_from_fat + grams_from_proteins + grams_from_carb

calories_per_gram = total_calories / food_grams

in_one_gram = (1 - (percent_water / 100)) * calories_per_gram

print(f'{in_one_gram:.4f}')

