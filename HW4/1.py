def makeSuffixArr(s):
    s = '\0' + s
    n = len(s)
    p = [i for i in range(n)]
    p.sort(key = lambda i : s[i])

    rank = [0] * n
    for i in range(1, n):
        rank[p[i]] = rank[p[i-1]] + (1 if s[p[i]] != s[p[i-1]] else 0)
    # print(p)
    # print(rank)
    rank_pair = [[0, 0] for i in range(n)]
    lenna = 1
    while lenna < n:
        for i in range(1, n):
            rank_pair[i] = [rank[i], rank[(i + lenna) % n]]
        p.sort(key = lambda i: rank_pair[i])
        rank[p[0]] = 0
        for i in range(1, n):
            rank[p[i]] = rank[p[i - 1]] + (1 if rank_pair[p[i]] != rank_pair[p[i - 1]] else 0)
        lenna *= 2
    return p


p = makeSuffixArr(input())
print(*p[1:])

