n, m = [int(x) for x in input().split()]
w = [int(x) for x in input().split()]
c = [int(x) for x in input().split()]
dp = [[-1] * (m + 1) for i in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    wi, ci = w[i - 1],  c[i - 1]
    for j in range(m + 1):
        dp[i][j] = dp[i - 1][j]
        if j - wi < 0 or dp[i-1][j-wi] == -1:
            continue
        if dp[i-1][j-wi] + ci > dp[i][j]:
            dp[i][j] = dp[i-1][j-wi] + ci

print(max(dp[-1]))