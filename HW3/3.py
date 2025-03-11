def z_funct(s):
    n = len(s)
    z = [0] * n
    z[0] = n
    l = r = 0
    for i in range(1,n):
        if i <= r:
            z[i] = min(r - i + 1,z[i-l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r:
            l = i
            r = i + z[i] - 1
    return z





z = z_funct(input())
ans = len(z)
for i in range(1, len(z)):
    if i + z[i] == len(z):
        ans = i
        break
print(ans)