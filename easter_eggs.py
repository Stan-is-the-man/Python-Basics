import sys

number_of_eggs = int(input())
red = 0
orange = 0
blue = 0
green = 0
max_eggs = -sys.maxsize
max_color = ''
for x in range(number_of_eggs):
    color = input()
    if color == 'red':
        red += 1
    elif color == 'orange':
        orange += 1
    elif color == 'blue':
        blue += 1
    elif color == 'green':
        green += 1

    if red > max_eggs:
        max_eggs = red
        max_color = "red"
    elif orange > max_eggs:
        max_eggs = orange
        max_color = "orange"
    elif blue > max_eggs:
        max_eggs = blue
        max_color = "blue"
    elif green > max_eggs:
        max_eggs = green
        max_color = "green"

print(f'Red eggs: {red}')
print(f'Orange eggs: {orange}')
print(f'Blue eggs: {blue}')
print(f'Green eggs: {green}')
print(f'Max eggs: {max_eggs} -> {max_color}')



