import sys
import math

number_of_kozunak = int(input())

max_used_flour = -sys.maxsize
max_used_sugar = -sys.maxsize
total_flour = 0
total_sugar = 0


for x in range(number_of_kozunak):
    sugar_quantity = int(input())
    flour_quantity = int(input())
    sugar_in_packs = sugar_quantity / 950
    total_sugar += sugar_in_packs
    flour_in_packs = flour_quantity / 750
    total_flour += flour_in_packs
    if sugar_quantity > max_used_sugar:
        max_used_sugar = sugar_quantity
    if flour_quantity > max_used_flour:
        max_used_flour = flour_quantity
print(f'Sugar: {math.ceil(total_sugar)}')
print(f'Flour: {math.ceil(total_flour)}')
print(f'Max used flour is {max_used_flour} grams, max used sugar is {max_used_sugar} grams.')


