import time, matplotlib.pyplot as plt
from lib.statistics import getStat
from lib.createPassword import createPassword

times = 5
digit = 5
option = 'NALUS'
arr = []
codeStart = time.time()

for i in range(times):
    password = createPassword(option, digit)
    start = time.time()

    while True:
        key = createPassword(option, digit)
        
        if key == password:
            end = time.time()
            elapsed = end - start
            arr.append(elapsed)

            print('[%d] Solved : %s - %fs' % (i + 1, key, elapsed))
            break

codeEnd = time.time()
codeElapsed = codeEnd - codeStart

print('%s%s_R Total Elapsed : %fs' % (digit, option, codeElapsed))
getStat(arr)

plt.hist(arr, bins=5, color='#E35F62')

plt.title('%d ASCII + Numbers + Special Characters (Random) / %d Times' % (digit, times))
plt.xlabel('Elapsed Time (s)')
plt.ylabel('Frequency')

plt.show()

f = open('./%s/%s%s_R.txt' % (option, digit, option), 'w')
for line in arr:
    f.write(str(line) + '\n')
f.close()