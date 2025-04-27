# a = list(map(int, input().split()))
#
# if a[-1] <= a[1]:
#     ans = a[0]
# else:
#     ans = (a[-1] - a[1]) * a[2] + a[0]
#
# print(ans)
#
#
# from attr.validators import matches_re
import re
maska = input()
ans = []
for i in range(5):
    ans.append(input())

new_m = maska.replace("?",".").replace("*",".*")
ans2 = []
for i in ans:
    if re.match(new_m,i):
        ans2.append("YES")
    else:
        ans2.append("NO")

for i in ans2:
    print(i)


# n = int(input())
# ans = [input().split() for i in range (n - 1)]
#
# dict = {}
#
# print(ans)
# for i in range(len(ans)):
#     if ans[i][0] == 'add':
#         if ans[i][2] not in dict:
#             dict[ans[i][2]] = ans[i][1]
#         else:
#             dict[ans[i][2]] += ans[i][1]
#     elif ans[i][0] == 'delete':
#         x = int(ans[i][1])
#
#         while x>0:




    # else:


# n= int(input())
# comanda = list(range(1,n + 1))
# rez = [int(input().split()[0]) for i in range(1, n -1)]
# print(rez)
# i = 0
# while len(comanda)>1:
#     dalshe = []
#     for j in range(0,len(comanda),2):
#         tmp = rez[i]
#         i +=1
#         if tmp == 1:
#             dalshe.append(rez[j])
#         else:
#             dalshe.append(comanda[j+1])
#
#     comanda = dalshe
#
# print(comanda[0])


