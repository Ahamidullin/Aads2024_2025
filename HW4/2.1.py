def compute_lcp(s, suffix_array):
    n = len(s)
    rank = [0] * n
    lcp = (n - 1) * [0]
    for i in range(n):
        rank[suffix_array[i]] = i
    h = 0
    for i in range(n):
        if rank[i] == n - 1:
            h = 0
            continue
        j = suffix_array[rank[i] + 1]
        while i + h < n and j + h < n and s[i + h] == s[j + h]:
            h += 1
        lcp[rank[i]] = h
        if h > 0:
            h -= 1

    return lcp

n = int(input())
s = input()

suffix_array = [int(x) - 1 for x in input().split()]
l_a = compute_lcp(s, suffix_array)
print(' '.join(map(str, l_a)))
