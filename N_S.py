import time, matplotlib.pyplot as plt
from lib.statistics import getStat
from lib.createPassword import createPassword

times = 1000
digit = 4
option = 'N'
arr = []
codeStart = time.time()

for i in range(times):
    password = createPassword(option, digit)
    start = time.time()

    for key in range(0, 10 ** digit):
        key = str(key).zfill(digit)
        
        if key == password:
            end = time.time()
            elapsed = end - start
            arr.append(elapsed)

            print('[%s] Solved : %s - %fs' % (i + 1, key, elapsed))
            break

codeEnd = time.time()
codeElapsed = codeEnd - codeStart

print('%s%s_S Total Elapsed : %fs' % (digit, option, codeElapsed))
getStat(arr)

plt.hist(arr, bins=2000, color='#E35F62')

plt.title('%d Numbers / %d Times' % (digit, times))
plt.xlabel('Elapsed Time (s)')
plt.ylabel('Frequency')

plt.show()

f = open('./Result/%s/%s%s_S.txt' % (option, digit, option), 'w')
for line in arr:
    f.write(str(line) + '\n')
f.close()