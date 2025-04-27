# s = input()
# t = input()
#
# newt = []
# news = []
#
# for i in t:
#     newt.append(int(ord(i)))
#
# for i in s:
#     news.append(int(ord(i)))
#
# res = ""
# for i in news:
#     if i in newt:
#         res += (chr(i))
# print(res)


# s = input()
# t = input()
#
#
# # for i in t:
# #     newt.append(int(ord(i)))
# #
# # for i in s:
# #     news.append(int(ord(i)))
#
# res = ""
# for i in s:
#     if i in t:
#         res += (i)
# print(res)

s = input()
t = input()

k = 0
dict = {}
for i in s:
    dict[i] = dict.get(i,k)
    k +=1
print(dict)

newt = sorted(t,key = lambda i:dict[i])
# key - правило по которому происходит сортировка
# sorted это цикл
# sorted сортирует по значению!!! которое выжает key то есть lambda
print(''.join(newt))