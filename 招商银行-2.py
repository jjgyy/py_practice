import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()

line1s = line1.split()
n = int(line1s[0])
k = int(line1s[1])

line2s = line2.split()
heights = []
for height_str in line2s:
    heights.append(int(height_str))

height_dict = {}
for height in heights:
    if height in height_dict:
        height_dict[height] += 1
    else:
        height_dict[height] = 1

height_enum = []
for key in height_dict:
    height_enum.append(key)
height_enum.sort()

cut_num = 0
cut_h = 1
cut_v = 0
cut_all_v = 0
while height_enum[-1] - cut_h >= 0:
    left_h = height_enum[-1] - cut_h
    last_cut_v = cut_v
    if left_h <= min(height_dict):
        print(cut_num + 1)
        break
    for key in height_dict:
        if left_h < key:
            cut_v += height_dict[key]
    if cut_v > k:
        cut_h -= 1
        cut_num += 1
        cut_all_v += last_cut_v
        cut_v = 0
    cut_h += 1

print(cut_num)