# как работает оператор with - контекстный менеджер
dict ={}

with open('input.txt') as f:
    for line in f.readlines():
        num,name = line.split()
        num = int(num)
        dict[num] = dict.get(num,[]) + [name]

# print(arr)

print(dict)

for key in sorted(dict):
    for value in dict[key]:
        print(key, value)



