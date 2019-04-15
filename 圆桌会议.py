import sys
line = sys.stdin.readline().strip()
nums = line.split()

# people
n = int(nums[0])
# start
s = int(nums[1])
# step
m = int(nums[2])

people = range(1, n + 1)
index = s - 1
for i in range(n):
    index = (index + m) % len(people)
    index -= 1
    print people[index]
    del people[index]
    if index == -1:  # the last element of link
        index = 0

