n1 = int(input())
arr1 = sorted(list(map(int, input().split())))

n2 = int(input())
arr2 = sorted(list(map(int, input().split())))

n3 = int(input())
arr3 = sorted(list(map(int, input().split())))

n4 = int(input())
arr4 = sorted(list(map(int, input().split())))


i = 0
j = 0
k = 0
t = 0
ans = [arr1[0], arr2[0],arr3[0],arr4[0]]

while (i < len(arr1) and j < len(arr2) and k < len(arr3) and t < len(arr4)):
    if arr1[i] == arr2[j] == arr3[k] == arr4[t]:
        ans[0] = arr1[i]
        ans[1] = arr2[j]
        ans[2] = arr3[k]
        ans[3] = arr4[t]
        break

    if abs(arr1[i] - arr2[j] - arr3[k] - arr4[t]) < abs(ans[0] - ans[1] - ans[2] -ans[3]):
        ans[0] = arr1[i]
        ans[1] = arr2[j]
        ans[2] = arr3[k]
        ans[3] = arr4[t]

    if arr1[i] > arr2[j]:
        j += 1
    elif arr1[i] > arr3[k]:
        k+=1
    elif arr1[i] > arr4[t]:
        t+=1
    else:
        i += 1

    if arr2[j] > arr3[k]:
        k += 1
    elif arr2[j] > arr4[t]:
        t += 1
    else:
        j += 1

    if arr3[k] > arr4[t]:
        t += 1
    else:
        k += 1





print(*ans)