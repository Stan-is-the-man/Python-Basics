target_height = int(input())
target_is_reached = False
current_target = target_height - 30
total_jump_counter = 0
current_jump_counter = 0
while current_jump_counter != 3:
    current_jump_height = int(input())
    total_jump_counter += 1
    if current_jump_height > target_height and current_target >= target_height:
        target_is_reached = True
        break
    elif current_jump_height > current_target:
        current_target += 5
        current_jump_counter = 0
    else:
        current_jump_counter += 1
if target_is_reached or current_target > target_height:
    print(f'Tihomir succeeded, he jumped over {current_target}cm after {total_jump_counter} jumps.')
else:
    print(f'Tihomir failed at {current_target}cm after {total_jump_counter} jumps.')