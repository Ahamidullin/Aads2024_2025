n = int(input())
suma = list(map(int,input().split()))

dp = [0] * (n + 1)

dp[1] = suma[0]

for i in range(2, n + 1):
    dp[i] = max(dp[i-1],dp[i-2]) + suma[i - 1]

print(dp[-1])

