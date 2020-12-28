import random, time, string, itertools, math, matplotlib.pyplot as plt
from statistics import getStat
from createPassword import createPassword

times = 100
digit = 4
option = 'NALU'
pool = string.digits + string.ascii_lowercase + string.ascii_uppercase
# pool = string.ascii_lowercase
arr = []
codeStart = time.time()

def numeral_system(number, base, digit):
    arr = []
    x = number
    for i in range(digit):
        div = x // base
        mod = x % base
        x = div
        arr.append(mod)

    return arr

for i in range(times):
    password = createPassword(option, digit)
    start = time.time()

    index = 0
    while True:
        temp = numeral_system(index, 26, digit)
        key = ''
        for j in temp[::-1]:
            key += pool[j]
        # print(key)
        
        if key == password:
            end = time.time()
            elapsed = end - start
            arr.append(elapsed)

            print('[%d] Solved : %s - %fs' % (i + 1, key, elapsed))
            break

        index += 1

codeEnd = time.time()
codeElapsed = codeEnd - codeStart

print('%s%s_S Total Elapsed : %fs' % (digit, option, codeElapsed))
getStat(arr)

plt.hist(arr, bins=1000, color='#E35F62')

plt.title('%d ASCII Lowercase / %d Times' % (digit, times))
plt.xlabel('Elapsed Time (s)')
plt.ylabel('Frequency')

plt.show()

f = open('./%s%s_S.txt' % (digit, option), 'w')
for line in arr:
    f.write(str(line) + '\n')
f.close()