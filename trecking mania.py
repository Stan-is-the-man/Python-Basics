number_members = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everest = 0
sum = 0
for x in range(number_members):
    people_number = int(input())
    if people_number <= 5:
        musala += people_number
    elif people_number <=12:
        monblan += people_number
    elif people_number <=25:
        kilimandjaro += people_number
    elif people_number <=40:
        k2 += people_number
    else:
        everest += people_number
sum = musala + monblan + kilimandjaro +k2 + everest
musala_percent = (musala / sum) * 100
monblan_percent = (monblan / sum) * 100
kilimandjaro_percent = (kilimandjaro / sum) * 100
k2_percent = (k2 / sum) * 100
everest_percent = (everest / sum) * 100

print(f'{musala_percent:.2f}%')
print(f'{monblan_percent:.2f}%')
print(f'{kilimandjaro_percent:.2f}%')
print(f'{k2_percent:.2f}%')
print(f'{everest_percent:.2f}%')
