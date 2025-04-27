
n = int(input())
money = list(map(int,input().split()))
money.sort(reverse = True)
print(money)
get = int(input())
n = get
ans = []
k = 0
for i in money:
    while i <= get:
        ans.append(i)
        get = get - i

if sum(ans) == n:

    print(len(ans))
    print(*ans)
else:
    print(-1)


