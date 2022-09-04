n = int(input())
m = int(input())
s = int(input())

for num in range(m, n, -1):
    if num != s:
        if num % 2 == 0 and num % 3 == 0:
            print(num, end=' ')
    elif num == s:
        break

