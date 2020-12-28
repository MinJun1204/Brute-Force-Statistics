import random
import time

codeStart = time.time()

for i in range(100):
    password = random.randint(0, 99999)
    start = time.time()

    while True:
        key = random.randint(0, 99999)
        if key == password:
            end = time.time()
            elapsed = end - start
            print('[%s] Solved : %s / %.4fs]' % (i + 1, key, elapsed))

            break
    # print(password)

codeEnd = time.time()
print(str(codeEnd - codeStart) + 's')