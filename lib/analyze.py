from statistics import getStat

arr = []
f = open('../NALUS/4NALUS_S.txt', 'r')
lines = f.readlines()
for line in lines:
    arr.append(float(line[0:-1]))
f.close()

getStat(arr)