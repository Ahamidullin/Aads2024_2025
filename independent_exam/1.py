a,b,c,d = map(int,input().split())

m = a * c
n = b * d

def gcd(m, n):
    if m == 0 or n == 0:
        return m + n
    if m >= n:
        return gcd(m - n,n)
    else:
        return gcd(m, n - m)

res = gcd(m, n)
print(m // res, n // res)