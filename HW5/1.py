n = int(input())
ans = [0] * 1001
ans[0] = 1
ans[1] = 1

for i in range(2, n + 1):
    ans[i] = (ans[i - 1] + ans[i - 2]) % 10

print(ans[n])
