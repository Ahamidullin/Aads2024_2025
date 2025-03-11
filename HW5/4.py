n = int(input())
a = [0] * (n + 1)
a[0] = 1
if n >= 1:
    a[1] = 1

for i in range(2, n + 1):
    if i % 2 == 0:
        a[i] = a[i // 2] + 1
    else:
        k = (i - 1) // 2
        a[i] = a[k] + a[k + 1] + 1

print(a[n])
