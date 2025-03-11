# def fib_digit(n):
#     if n == 0:
#         return 0
#     elif n <= 2:
#         return 1
#     else:
#         ans = [0] * (n + 1)
#         ans[0], ans[1] = 0, 1
#         for i in range(2, n + 1):
#             ans[i] = (ans[i - 1] + ans[i - 2]) % 10
#     return ans[i]
#
#
# def main():
#     n = int(input())
#     print(fib_digit(n))
#
#
# if __name__ == "__main__":
#     main()
# def isPowerOfTwo(n):
#     if n == 0:
#         return False
#     elif n == 1:
#         return True
#     else:
#         cnt = 2
#         ans = 1 # сктпень
#         while n >= cnt:
#             cnt = 2 ** ans
#             if n == cnt:
#                 return True
#             ans +=1
#         return False
def isPowerOfTwo(n):
    cnt = 0
    res = 1
    if res == n:
        return True
    elif res > n:
        return False
    else:
        cnt +=1
        res = isPowerOfTwo(2**cnt)



print(isPowerOfTwo(int(input())))