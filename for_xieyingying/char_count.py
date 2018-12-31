# encoding=utf-8
s = "abcdefgababejdsxcdaswcdfeewfsadscdfffsdsadsaczccaasdwscxzcsadwdaswqdsa"
count_dic = {}
for c in s:
    if c not in count_dic:
        count_dic[c] = 1
    else:
        count_dic[c] = count_dic[c] + 1

for key in count_dic:
    print key, ":", count_dic[key]


# 拓展练习：如果需要按照出现的顺序，从高至低排序呢？，可留作明天练习