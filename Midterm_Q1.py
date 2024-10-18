def above_average_counter(input, output):
   
    with open(input, 'r') as file:
        lines = file.readlines()

    students = []
    grades = []

    for line in lines:
        name, grade = line.split()
        grade = int(grade)
        students.append((name, grade))
        grades.append(grade)

    # Calculate the average grade
    if grades:
        av_grade = sum(grades) / len(grades)
    else:
        av_grade = 0

     above_average_count = 0

     for grade in grades:
        if grade > av_grade:
            above_average_count += 1

    
    with open(output, 'w') as file:
        file.write(f"Average Grade: {av_grade:.2f}\n")
        file.write(f"Number of Students Above Average: {above_average_count}\n")

above_average_counter('grades.txt', 'results.txt')
