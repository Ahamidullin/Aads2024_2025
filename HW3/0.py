import scipy.stats as stats

# n = int(input())
# z_nums = [int(i) for i in input().split()]
# i = 0
# while i < n:
#     if z_nums[i] > 1:
#         for j in range(1, z_nums[i] + 1):
#             z_nums[i] = j
#             i += 1
#     else:
#         i += 1
# print(*z_nums)
# def z_to_prefix(n, z):
#     # Инициализация префикс-функции
#     pi = [0] * n
#
#     for i in range(1, n):
#         if z[i] > 0:
#             for j in range(z[i]):
#                 if pi[i + j] == 0:
#                     pi[i + j] = j + 1
#                 else:
#                     break
#
#     return pi
#
#
# # Ввод данных
# n = int(input())
# z = list(map(int, input().split()))
#
# # Вычисление префикс-функции
# pi = z_to_prefix(n, z)
#
# # Вывод результата
# print(*pi)

# n = int(input())
# z = list(map(int, input().split()))
# pi = [0] * n
#
# for i in range(1, n):
#     if z[i] > 0:
#         for k in range(z[i]):
#             if pi[i + k] >= k + 1:
#                 break
#             pi[i + k] = k + 1
#
# for i in range(1, n):
#     if pi[i] > pi[i - 1] + 1:
#         pi[i] = pi[i - 1] + 1
#
# print(*pi)


#abracadabra
#00010101234


#
# # Data
# xi = [7.72, 9.58, 12.38, 7.77, 11.27, 8.80, 11.10, 7.80, 10.17, 6.00, 12.12]
# n = len(xi)  # Number of observations
# mu = 9.52  # Known mean
#
# # Step 1: Calculate the sum of squared deviations from the mean
# sum_squared_deviations = sum((x - mu) ** 2 for x in xi)
#
# # Step 2: Degrees of freedom
# df = n
#
# # Step 3: Find chi-squared critical values for 95% confidence level
# alpha = 0.05
# chi2_lower = stats.chi2.ppf(alpha / 2, df)
# chi2_upper = stats.chi2.ppf(1 - alpha / 2, df)
#
# # Step 4: Calculate confidence interval for variance
# variance_lower = sum_squared_deviations / chi2_upper
# variance_upper = sum_squared_deviations / chi2_lower
#
# print(variance_lower, variance_upper)
# print(sum_squared_deviations / 3.816)
const = 22.86 / 10
flag = 1
for i in range(1,11):
    if (const + 0.45 * i) >= 4 and flag == 1:
        print(i, const + 0.45 * i)
        flag = 0
    if (const + 0.45 * i) >= 6:
        print(i,const + 0.45 * i)
        break

print(6-const/0.45)