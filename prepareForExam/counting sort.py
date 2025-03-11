# III. COUNT sort O(n+k)
def countSort(array, func=lambda x: x):
    # First step: initialize all arrays (incl. count bins)
    k = len(array)
    output = [0] * len(array)
    count = [0] * 10

    # Second step: count appearance of each value & where it should stand
    for i in range(k): count[func(array[i])] += 1
    for i in range(1, 10): count[i] += count[i-1]

    # Third step: place all elements on the respective place
    for i in range(k-1,-1,-1):
        output[count[func(array[i])] - 1] = array[i]
        count[func(array[i])] -= 1

    for i in range(k): array[i] = output[i]
    return array