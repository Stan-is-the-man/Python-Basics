max_bad_grades = int(input())
bad_grades = 0
average_grade = 0
number_of_problems = 0
last_problem = ''
is_expelled = False

current_problem = input()

while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades += 1
        if bad_grades == max_bad_grades:
            is_expelled = True
            break
    number_of_problems += 1
    average_grade += current_grade
    last_problem = current_problem
    current_problem = input()

if is_expelled:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    average_grade /= number_of_problems
    print(f'Average score: {average_grade:.2f}')
    print(f'Number of problems: {number_of_problems}')
    print(f'Last problem: {last_problem}')
