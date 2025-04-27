n = int(input())
arr = list(map(int, input().split()))

if n == 0:
    print(0)


elif n == 1:
    print(arr[0])

else:
    ans = [0] * (n)
    ans[0] = arr[0]
    ans[1] = arr[1]

    for i in range(2, n):
        ans[i] = arr[i] + min(ans[i - 1], ans[i - 2])

    print(ans[-1])
