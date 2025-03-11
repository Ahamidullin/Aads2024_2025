
def SelectionSort(A):
    res = []
    while A:
        max_index = 0
        max = A[0]

        for i in range(1, len(A)):
            if A[i] > max:
                max = A[i]
                max_index = i
        res.append(max)
        A.pop(max_index)

    return res

arr = list(map(int, input().split()))

print(*SelectionSort(arr))