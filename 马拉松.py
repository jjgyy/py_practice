import sys
line1 = sys.stdin.readline().strip()
inputs1 = line1.split()

n = int(inputs1[0])
v = int(inputs1[1])

starts = []
ends = []

for _ in range(n):
    line = sys.stdin.readline().strip()
    inputList = line.split()
    starts.append(int(inputList[0]))
    ends.append(int(inputList[1]))
results = []
for index in range(n):
    length = 0
    vv = v
    while vv > 0:
        length += ends[index] - starts[index]
        if index != n - 1:
            length += min(vv, starts[index+1] - ends[index])
            vv -= starts[index+1] - ends[index]
        else:
            length += vv
            break

    results.append(length)

print(max(results))
