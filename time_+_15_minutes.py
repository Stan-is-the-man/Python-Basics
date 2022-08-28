hours = int(input())
minutes = int(input())

minutes += 15           # minutes = minutes + 15
#превръщаме минути в часове и ако е над 1 час се добавя към hours
hours += minutes // 60  # hours = hours + minutes // 60

minutes %= 60

# ako e na granica 23:59, chasa da stane 0
if hours > 23:
    hours = 0

if minutes < 10:
    print(f"{hours}:0{minutes}")
else:
    print(f"{hours}:{minutes}")