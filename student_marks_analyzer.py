marks = []

n = int(input("Enter number of students: "))

for i in range(n):
    mark = int(input("Enter mark of student: "))
    marks.append(mark)

average = sum(marks) / len(marks)
highest = max(marks)
lowest = min(marks)

print("Average marks:", average)
print("Highest mark:", highest)
print("Lowest mark:", lowest)
