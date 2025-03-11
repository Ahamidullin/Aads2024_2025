def z_function(s):
    z = [0] * len(s)
    z[0] = len(s)

    for i in range(1, len(s)):
        cnt = 0
        while i + cnt < len(s) and s[cnt] == s[i + cnt]:
            cnt += 1
        z[i] = cnt

    return z



print(z_function(input()))
