import sys
line = sys.stdin.readline().strip()

inputs = line.split()

n = int(inputs[0])
m = int(inputs[1])

edges = []
for _ in range(m):
    line = sys.stdin.readline().strip()
    inputs = line.split()
    edges.append([int(inputs[0]), int(inputs[1])])

point_enter_dict = {}
p = {}

for point in range(1, n+1):
    point_enter_dict[point] = 0
    p[point] = 0

for edge in edges:
    edge_end = edge[1]
    point_enter_dict[edge_end] += 1

graph_begin = 0

for point in point_enter_dict:
    if point_enter_dict[point] == 0:
        graph_begin = point
        break

p[graph_begin] = 1
canntStop = True
while canntStop:
    canntStop = False
    dirty = True
    while dirty:
        dirty = False
        for edge in edges:
            edge_begin = edge[0]
            edge_end = edge[1]
            if p[edge_end] <= p[edge_begin]:
                p[edge_end] = p[edge_begin] + 1
                dirty = True

    values = []
    for point in range(1, n+1):
        if p[point] in values:
            p[point] += 1
            canntStop = True
        values.append(p[point])


result = []
for point in range(1, n+1):
    result.append(p[point])

print " ".join(str(e) for e in result)
