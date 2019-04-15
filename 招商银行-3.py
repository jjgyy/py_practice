import sys
n = input()
line = sys.stdin.readline().strip()
lines = line.split()
nums = []
for num_str in lines:
    nums.append(int(num_str))

fushu = []
zhengshu = []
for num in nums:
    if num < 0:
        fushu.append(num)
    else:
        zhengshu.append(num)

if len(zhengshu) == 1:
    print (-sum(fushu)) + zhengshu[0]
else:
    print sum(zhengshu) - (2*min(zhengshu)) - sum(fushu)