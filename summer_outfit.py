degrees = int(input())
daytime = input()

outfit = ''
shoes = ''

if daytime == 'Morning':
    if 10 <= degrees <= 18:
        outfit = "Sweatshirt"
        shoes = 'Sneakers'
    elif degrees <= 24:
        outfit = "Shirt"
        shoes = 'Moccasins'
    else:
        outfit = "T-Shirt"
        shoes = 'Sandals'

elif daytime == 'Afternoon':
    if 10 <= degrees <= 18:
        outfit = "Shirt"
        shoes = 'Moccasins'
    elif degrees <= 24:
        outfit = "T-Shirt"
        shoes = 'Sandals'
    else:
        outfit = "Swim Suit"
        shoes = 'Barefoot'

else:
    outfit = "Shirt"
    shoes = 'Moccasins'

print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")



