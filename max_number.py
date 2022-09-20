import sys
num = 0
max_number = -sys.maxsize
while True:
    num = input()

    if num == "Stop":
        break

    if int(num) > max_number:
        max_number = int(num)

print(max_number)


