def countingSort(arr):
    minDistance = -10000
    maxDistance = 10000
    copacity = maxDistance - minDistance +1
    cntNum = [0] * copacity

    for num in arr:
        cntNum[num + len(cntNum)//2] += 1

    res = []
    for num in range(copacity):
        res.extend(cntNum[num] * [num + minDistance])

    return res

n = int(input())
arr = list(map(int, input().split()))
print(*countingSort(arr))