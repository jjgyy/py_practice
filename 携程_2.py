import sys
line = sys.stdin.readline().strip()

inputs = line.split()

stack = []
minStack = []
maxStack = []

for e in inputs:
    if e == '#':
        if stack == []:
            continue
        re = stack.pop()
        if minStack[-1] == re:
            minStack.pop()
        if maxStack[-1] == re:
            maxStack.pop()
        continue
    else:
        int_e = int(e)
        stack.append(int_e)
        if (minStack == []) or (int_e <= minStack[-1]):
            minStack.append(int_e)
        if (maxStack == []) or (int_e >= maxStack[-1]):
            maxStack.append(int_e)
        continue

if stack == []:
    print "the stack is empty"
else:
    print str(maxStack[-1]) + " " + str(minStack[-1])
