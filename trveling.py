destination = input()
budget = float(input())

current_sum = 0
current_command = ''

while current_sum <= budget:
    current_command = input()

    current_saving = float(current_command)
    current_sum += current_saving
    if current_sum >= budget:
        print(f'Going to {destination}!')
        current_sum = 0
        destination = input()
        if destination == "End":
            break
        budget = float(input())



