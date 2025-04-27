def f(q):
    ans = []
    dict = {}
    for i in range(len(q)):
        if q[i][0] == 'add':
            dict[int(q[i][1])] = q[i][2]

        elif q[i][0] == 'del':
            # удаление происходит по ключу
            if int(q[i][1]) in dict:
                del dict[int(q[i][1])]
        else:
            if int(q[i][1]) in dict:
                ans.append(dict[int(q[i][1])])
            else:
                ans.append("not found")
    return ans

n = int(input())
q = [input().split() for i in range(n)]
# print(q)
print(*f(q), sep = '\n')

