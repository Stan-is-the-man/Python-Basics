player_one = int(input())
player_two = int(input())
player_three = int(input())

total_time = player_one + player_two + player_three

mins = total_time // 60
secs = total_time % 60
if secs < 10:
    print(f"{mins}:0{secs}")

else:
    print(f"{mins}:{secs}")

