destination = input()
period = input()
number_of_nights = int(input())


if destination == "France":
    if period == "21-23":
        price = number_of_nights * 30
    elif period == "24-27":
        price = number_of_nights * 35
    elif period == "28-31":
        price = number_of_nights * 40
        
elif destination == "Italy":
    if period == "21-23":
        price = number_of_nights * 28
    elif period == "24-27":
        price = number_of_nights * 32
    elif period == "28-31":
        price = number_of_nights * 39
        
else:
    if period == "21-23":
        price = number_of_nights * 32
    elif period == "24-27":
        price = number_of_nights * 37
    elif period == "28-31":
        price = number_of_nights * 43

print(f'Easter trip to {destination} : {price:.2f} leva.')
