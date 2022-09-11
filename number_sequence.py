import sys

n = int(input())
min = sys.maxsize
max = -sys.maxsize

for x in range(n):
    num = int(input())

    if num < min:
        min = num

    if num > max:
        max = num

print(f'Max number: {max}')
print(f'Min number: {min}')



