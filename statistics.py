import math

def getStat(arr):
    arr.sort()
    mean = sum(arr) / len(arr)
    temp = 0

    for i in arr:
        temp = temp + (i - mean) ** 2

    variance = temp / len(arr)
    std = math.sqrt(variance)

    index = int(len(arr) / 2)
    if len(arr) % 2 == 1:
        median = arr[index]
    else:
        median = (arr[index - 1] + arr[index]) / 2.0

    Sk = (3 * (mean - median)) / std
    if Sk < 0:
        dist = '왼쪽'
    else:
        dist = '오른쪽'

    print('평균 : %fs | 분산 : %f | 표준편차 : %f | 중앙값 : %fs | 비대칭도 : %f | %s 꼬리분포' % (mean, variance, std, median, Sk, dist))