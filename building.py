floors = int(input())
rooms = int(input())
counter = 0
for f in range(floors, 0, -1):
    for r in range(rooms):
        if f == floors and counter == 0:
            print(f'L{f}{r} ', end='')
        elif f % 2 == 0:
            print(f"O{f}{r} ", end='')
        else:
            print(f"A{f}{r} ", end='')
