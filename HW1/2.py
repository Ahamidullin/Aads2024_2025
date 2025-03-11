# n = int(input())
# arr1 = list(map(int, input().split()))
#
# m = int(input())
# arr2 = list(map(int,input().split()))
#
# mindif = float("inf")
# num1 = 0
# num2 = 0
# for i in range(len(arr1)):
#     for j in range(len(arr2)):
#         if(mindif >abs(arr1[i]-arr2[j])):
#             mindif = abs(arr1[i]-arr2[j])
#             num1 = arr1[i]
#             num2 = arr2[j]
#             # print( num1,num2)
#
# print(num1,num2)


n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

i = 0
j = 0
ans = [arr1[0], arr2[0]]

while (i < len(arr1) and j < len(arr2)):
    if arr1[i] == arr2[j]:
        ans[0] = arr1[i]
        ans[1] = arr2[j]
        break

    if abs(arr1[i] - arr2[j]) < abs(ans[0] - ans[1]):
        ans[0] = arr1[i]
        ans[1] = arr2[j]

    if arr1[i] > arr2[j]:
        j += 1
    else:
        i += 1
print(*ans)
