n = int(input())
cost = [0] + list()
dp = [0] * 1001
dp[1] = cost[1]

for i in range(2, n):
    dp[i] = min(dp[i-1], dp[i-2]) + cost[i]

print(*dp)
