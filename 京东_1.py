import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
line3 = sys.stdin.readline().strip()

inputs1 = line1.split()
inputs2 = line2.split()
inputs3 = line3.split()

n = int(inputs1[0])
V = float(inputs1[1])

ratios = []
for e in inputs2:
    ratios.append(float(e))

materials = []
for e in inputs3:
    materials.append(float(e))

bili = materials[0] / ratios[0]
for index in range(n):
    bili = min(bili, materials[index] / ratios[index])

result = 0.0
for ratio in ratios:
    result += ratio * bili

result = min(result, V)

print("%.4f"%result)