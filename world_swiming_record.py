world_record = float(input())
distance_in_meters = float(input())
secs_per_meter = float(input())

added_secs_for_friction = distance_in_meters // 15 * 12.5

distance_to_swim = distance_in_meters * secs_per_meter + added_secs_for_friction

if distance_to_swim < world_record:
    print(f"Yes, he succeeded! The new world record is {distance_to_swim:.2f} seconds.")

elif distance_to_swim >= world_record:
    seconds_to_record = distance_to_swim - world_record
    print(f'No, he failed! He was {seconds_to_record:.2f} seconds slower.')
