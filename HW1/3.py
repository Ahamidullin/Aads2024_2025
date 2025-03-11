def merge(ans):
    if len(ans) ==1:
        return ans

    mid = len(ans) // 2
    x1 = ans[:mid]
    x2 = ans[mid:]

    x1 = merge(x1)
    x2 = merge(x2)

    i = 0
    j = 0
    res = []

    while (i < len(x1) and j < len(x2)):
        if x1[i] >= x2[j]:
            res.append(x2[j])
            j+=1
        else:
            res.append(x1[i])
            i += 1

    if i == len(x1):
        res.extend(x2[j:])  # Добавляем остатки x2
    else:
        res.extend(x1[i:])  # Добавляем остатки x1

    return res



n = int(input())

ans = list(map(int, input().split()))

print(*merge(ans))





