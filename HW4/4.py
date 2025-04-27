# # Реализуйте структуру данных, которая поддерживает следующие операции:
# #
# # добавить в словарь строку S;
# # найти в словаре k-ю строку в лексикографическом порядке.
# # Известно, что изначально словарь пуст.
from unicodedata import numeric

n = int(input())
# options = [int(i) if (i:=input()).isnumeric() else i for _ in range(int(input()))]
ans = []
for i in range(n):
    x = input()
    if x.isnumeric():
        ans.sort()
        print(ans[int(x)- 1])
    else:
        ans.append(x)

# print(ans1, sorted(ans2))



    # i = 0
    # while i < len(arr1):
    #     print(arr2[arr1[i] - 1])
    #     i += 1


#
#
#
#
# n = int(input())
# authors = []
# for _ in range(n):
#     option = input()
#     if option.isnumeric():
#         authors.sort()
#         print(authors[int(option)-1])
#     else:
#         authors.append(option)