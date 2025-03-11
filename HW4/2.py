n = int(input())
s = input()
num = list(map(lambda x: int(x) - 1,input().split()))
# num = [int(i) - 1 for i in input().split()]
print(num)

def f(index1, index2):
    cnt = 0
    while s[index1] == s[index2] and index1 < n and index2 < n:
        cnt +=1
        index1 += 1
        index2 += 1
    return cnt

# ans = []
# for i in zip(num, num[1:]):
#     # print(i)
#     ans.append(f(*i))
# print(*ans)

print([f(*i) for i in zip(num, num[1:])])