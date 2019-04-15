n = input()
n = int(n)
students = []
for _ in range(n):
    height = input()
    students.append(int(height))

for index in range(n):
    if index == n - 1:
        print(0)
        break
    higher = -1
    for i in range(index + 1, n):
        if students[i] > students[index]:
            higher = i
            break
    print(higher + 1)
