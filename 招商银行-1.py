import sys
line1 = sys.stdin.readline().strip()
line2 = sys.stdin.readline().strip()
line3 = sys.stdin.readline().strip()
n = int((line1.split())[0])
legs_str = line2.split()
powers_str = line3.split()
legs = []
powers = []
for leg in legs_str:
    legs.append(int(leg))
for power in powers_str:
    powers.append(int(power))

leg_dict = {}
for leg in legs:
    if leg in leg_dict:
        leg_dict[leg] += 1
    else:
        leg_dict[leg] = 1


