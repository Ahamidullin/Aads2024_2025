n = int(input())
s = input()
char_count = {}
min_odd_val = float("inf")
min_odd_keys = []
min_letter = ''

for i in s:
    char_count[i] = char_count.get(i, 0) + 1
print(char_count)


for key, value in char_count.items():
    if value % 2 == 1:
        min_odd_keys.append(key)
print(min_odd_keys)
if len(min_odd_keys) != 0:
    min_letter = min(min_odd_keys)
# print(min_letter)

ans = ''
for i in sorted(char_count):
    ans += i * (char_count[i] // 2)
print(ans + min_letter + ans[::-1])
