import csv

marks = []

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        marks.append(int(row['marks']))

total = sum(marks)
average = total / len(marks)

print("Marks:", marks)
print("Total:", total)
print("Average:", average)

if average >= 75:
    print("Good Performance ✅")
else:
    print("Needs Improvement ❌")
