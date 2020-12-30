import time, string, matplotlib.pyplot as plt
from lib.statistics import getStat
from lib.createPassword import createPassword

times = 100000
digit = 3
option = 'NALUS'

if option == 'AL':
    pool = string.ascii_lowercase
elif option == 'NALU':
    pool = string.digits + string.ascii_lowercase + string.ascii_uppercase
elif option == 'NALUS':
    pool = string.printable

arr = []
codeStart = time.time()

def numeral_system(number, base, digit):
    result = []
    x = number
    for i in range(digit):
        div = x // base
        mod = x % base
        x = div
        result.append(mod)
        result.reverse()

    return result

for i in range(times):
    password = createPassword(option, digit)
    start = time.time()

    index = 0
    while True:
        temp = numeral_system(index, 100, digit)
        key = ''
        for j in temp:
            key += pool[j]
        
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

plt.hist(arr, bins=500, color='#E35F62')

plt.title('%d ASCII + Numbers + Special Characters (Sequential) / %d Times' % (digit, times))
plt.xlabel('Elapsed Time (s)')
plt.ylabel('Frequency')

plt.show()

f = open('./Result/%s/%s%s_S.txt' % (option, digit, option), 'w')
for line in arr:
    f.write(str(line) + '\n')
f.close()