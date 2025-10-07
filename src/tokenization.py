def tokenization(s):
    """Функция для токенизации. Составляет список из чисел и знаков и
    переводит числа в int или float."""
    s = s.replace(' ', '')
    s = [x for x in s]
    i = 1
    while i < len(s):
        if s[i - 1][0] in "0123456789.":
            if s[i] in "0123456789.":
                s[i - 1] = s[i - 1] + s[i]
                s.pop(i)
            else:
                i += 1
        elif s[i] in "*/":
            if s[i - 1] in "*/":
                s[i - 1] = s[i] + s[i - 1]
                s.pop(i)
            else:
                i += 1
        else:
            i += 1
    for i in range(len(s)):
        if '.' in s[i]:
            s[i] = float(s[i])
        elif s[i].isdigit():
            s[i] = int(s[i])
    return s
