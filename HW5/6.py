# from itertools import product
# def f(n,b):
#     string = ''
#     while n > 0:
#         string += str(n % b)
#         n //= 3
#     return(string[::-1])
# n = int(input())
# cnt = 0
#
# for i in product("ABC", repeat = n):
#     if ("AA" not in ''.join(i)):
#         cnt+=1
#         print(i)
#
# print(n,cnt, bin(cnt)[2::],f(cnt,3))
#
#


n = int(input())

ans = [0] * (n+1)
ans[0] = 3
ans[1] = 8

for i in range(2, n + 1):
    ans[i] = (ans[i-1] + ans[i -2]) * 2

print(ans[-2])