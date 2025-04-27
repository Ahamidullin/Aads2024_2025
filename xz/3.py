# Вход в функцию
d = {
   'b' : 4,
   'c' : {
       'd': 3,
       'e': 5,
    }
}

# Пример выхода
# [
# ('b', 4),
# ('c.d', 3),
# ('c.e', 5),
# ]

def f(dictinary):
    l = []
    for key, value in dictinary.items():
        if not (isinstance(value, dict)):
            l.append((key, value))
        else:
            s = f(value)
            l.extend(s)
    return l
print(f(d))
