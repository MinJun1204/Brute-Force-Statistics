import matplotlib.pyplot as plt

digit = 4
times = 10
option = 'NALUS'
type = 'S'

arr = []
f = open('../%s/%d%s_%s.txt' % (option, digit, option, type), 'r')
lines = f.readlines()
for line in lines:
    arr.append(float(line[0:-1]))
f.close()

plt.hist(arr, bins=50, color='#E35F62')

plt.title('%d ASCII + Numbers + Special Characters (Sequential) / %d Times' % (digit, times))
plt.xlabel('Elapsed Time (s)')
plt.ylabel('Frequency')

plt.show()