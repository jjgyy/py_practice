import sys
line1 = sys.stdin.readline().strip()
inputs1 = line1.split()

line2 = sys.stdin.readline().strip()
inputs2 = line2.split()

peopleNum = int(inputs1[0])
askNum = int(inputs1[1])

peoples = []
for e in inputs2:
    peoples.append(int(e))

asks = []
asksDic = {}
for _ in range(askNum):
    ask = input()
    asks.append(int(ask))
    asksDic[int(ask)] = 0

peoples.sort()
for index in range(peopleNum):
    peoples[index] = peoples[index] - index - 1
    if peoples[index] in asks:
        asksDic[peoples[index]] += 1
for ask in asks:
    print(asksDic[ask])
