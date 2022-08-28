hour_of_exam = int(input())
mins_of_exam = int(input())
hour_of_arriving = int(input())
mins_of_arriving = int(input())

time_of_exam = hour_of_exam * 60 + mins_of_exam
time_of_arriving = hour_of_arriving * 60 + mins_of_arriving

if time_of_arriving > time_of_exam:
    print('Late')
elif time_of_exam - 30 <= time_of_arriving <= time_of_exam:
    print('On time')
else:
    print('Early')

diff = abs(time_of_arriving - time_of_exam)

if time_of_exam - 60 < time_of_arriving < time_of_exam:
    print(f'{diff} minutes before the start')
elif time_of_exam - 60 >= time_of_arriving:
    hours = diff // 60
    mins = diff % 60
    if mins < 10:
        print(f'{hours}:0{mins} hours before the start')
    else:
        print(f'{hours}:{mins} hours before the start')
elif time_of_exam < time_of_arriving < time_of_exam + 60:
    print(f'{diff} minutes after the start')
elif time_of_arriving > time_of_exam + 60:
    hours = diff // 60
    mins = diff % 60
    if mins < 10:
        print(f'{hours}:0{mins} hours after the start')
    else:
        print(f'{hours}:{mins} hours after the start')
