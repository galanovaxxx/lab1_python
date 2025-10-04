def token_function(s: str) -> list:
    """Функция для токенизации. Составляет список из чисел и знаков и
    переводит числа в int или float."""
    s = s.replace(' ', '') # убираем пробелы
    s = [x for x in s] # переводим строчку в список генератором
    i = 1 # индекс списка
    while i < len(s):
        if s[i - 1][0] in "0123456789.":
            if s[i] in "0123456789.":
                s[i - 1] = s[i - 1] + s[i] # "склеиваем" цифры в числа 
                s.pop(i)
            else:
                i += 1
        elif s[i] in "*/":
            if s[i - 1] in "*/":
                s[i - 1] = s[i] + s[i - 1] # "склеиваем" * и * или / и /
                s.pop(i)
            else:
                i += 1
        else:
            i += 1
    for i in range(len(s)): # переводем числа в int или в float
        if '.' in s[i]:
            s[i] = float(s[i])
        elif '0' in s[i] or '1' in s[i] or '2' in s[i] or '3' in s[i] or '4' in s[i] or '5' in s[i] or '6' in s[
            i] or '7' in s[i] or '8' in s[i] or '9' in s[i]:
            s[i] = int(s[i])
    return s
