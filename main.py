IS_ORDERED = False
MAX_LEN = 12

with open("dict.txt") as file:
    words = [w.lower().strip() for w in file.read().split('\n')]

s = input('>>> ').lower()

result = []
if IS_ORDERED:
    s_lst = list(s[::-1])
    for word in words:
        with_caps = ''
        temp_s = s_lst.copy()
        for c in word:
            if temp_s and c == temp_s[-1]:
                temp_s.pop(-1)
                with_caps += c.upper()
            else:
                with_caps += c.lower()
        if not temp_s and len(word) <= MAX_LEN:
            result.append(with_caps)
else:
    allowed = {}
    for c in s:
        if c not in allowed:
            allowed[c] = 1
        else:
            allowed[c] += 1
    for word in words:
        with_caps = ''
        temp_allowed = allowed.copy()
        for c in word:
            if c in temp_allowed and temp_allowed[c] >= 1:
                temp_allowed[c] -= 1
                with_caps += c.upper()
            else:
                with_caps += c.lower()
        if all(v == 0 for v in temp_allowed.values()) and len(word) <= MAX_LEN:
            result.append(with_caps)

for i in range(len(result)):
    spaces = ' ' * (len(str(len(result))) - len(str(i + 1)) + 1)
    print(f'{i + 1}.{spaces}{result[i]}')
