n = int(input())


ans = [0] * 1001
ans[0] = 1
ans[1] = 1


for i in range(2, n + 1):
    if (i % 2 == 0):
        ans[i] = ans[i // 2] + ans[i // 2 - 1]
    else:
        ans[i] = ans[i // 2] - ans[i // 2 - 1]

print(ans[n])