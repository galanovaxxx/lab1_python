def in_brackets(s, sign: [list, str]) -> [str, bool]:
    balance = 0
    if sign in s[1:]:
        for x in range(len(s)):
            if s[x] == '(':
                balance += 1
            if s[x] == ')':
                balance -= 1
            if s[x] == sign and x != 0:
                if balance == 0:
                    return x
    return False


def expr(s: list) -> [int, float]:
    """Функция убирает скобки, окаймляющие список, если скобки есть
    и список не пустой. Потом вызывает функцию add."""
    balance = 0  # проверка скобок
    flag = 1  # флаг для проверки, закрывается ли первая скобка
    if '(' in s and s:
        for i in range(len(s)):
            if s[i] == '(':
                balance += 1
            if s[i] == ')':
                balance -= 1
            if i > 0 and i != len(s) - 1:
                if balance == 0:
                    flag = 0
        if flag == 1:
            s = s[1:-1]  # удаляем скобки, если они окаймляют выражение
    return add(s)


def add(s: list) -> [int, float]:
    """Функция находит '+' или '-' находящееся не в скобках и снова
    вызывает эту функцию от частей списка до и после найденых элементов.
    Если элементов в списке нет, вызывает другую функцию."""
    balance = 0
    if '+' in s[1:]:
        x = in_brackets(s, '+')
        if x:  # если + находится не в скобках
            return add(s[:x]) + add(s[x + 1:])  # вызываем функцию от срезов и складываем

    if '-' in s[1:]:
        x = in_brackets(s, '-')
        if x:  # если - находится не в скобках
            return add(s[:x]) - add(s[x + 1:])  # вызываем функцию от срезов и вычитаем
    return mul(s)


def mul(s: list) -> [int, float]:
    """Функция находит '*', или '/', или '//', или '%' аходящееся не в скобках и
    снова вызывает эту функцию от частей списка до и после найденых элементов.
    Если элементов в списке нет, вызывает другую функцию."""
    if '*' in s:
        x = in_brackets(s, '*')
        if x:  # если * находится не в скобках
            return mul(s[:x]) * mul(s[x + 1:])  # вызываем функцию от срезов и умножаем
    if '/' in s:
        x = in_brackets(s, '/')
        if x:  # если / находится не в скобках
            if mul(s[x + 1:]) != 0:
                return mul(s[:x]) / mul(s[x + 1:])  # вызываем функцию от срезов и делим
            else:
                raise ZeroDivisionError("Деление на ноль")
    if '//' in s:
        x = in_brackets(s, '//')
        if x:  # если // находится не в скобках
            if mul(s[x + 1:]) != 0 and int(mul(s[:x])) == mul(s[:x]) and int(mul(s[x + 1:])) == mul(s[x + 1:]):
                return mul(s[:x]) // mul(s[x + 1:])  # вызываем функцию от срезов и делим нацело
            elif mul(s[x + 1:]) == 0:
                raise ZeroDivisionError("Деление на ноль")
            else:
                raise ValueError("Ошибка при делении")
    if '%' in s:
        x = in_brackets(s, '%')
        if x:  # если % находится не в скобках
            if mul(s[x + 1:]) != 0 and int(mul(s[:x])) == mul(s[:x]) and int(mul(s[x + 1:])) == mul(s[x + 1:]):
                return mul(s[:x]) % mul(s[x + 1:])  # вызываем функцию от срезов и находим остаток от деления
            elif mul(s[x + 1:]) == 0:
                raise ZeroDivisionError("Деление на ноль")
            else:
                raise ValueError("Ошибка при делении")
    return pow(s)


def pow(s: list) -> [int, float]:
    """Функция находит '**', находящееся не в скобках и снова вызывает эту функцию
    от частей списка до и после '**'. Если '**' нет в списке, вызывает другую функцию"""
    if '**' in s:  # если в s есть **
        x = in_brackets(s, '**')
        if x:  # если ** находится не в скобках
            return pow(s[:x]) ** pow(s[x + 1:])  # вызываем функцию от срезов и возводим в степень
    return unary(s)


def unary(s: list) -> [int, float]:
    """Функция работает с унарными знаками. Если '+', удаляет его, если '-', удаляет его
    и умножает следующее за ним число на (-1)."""
    if s:  # если s не пустой
        if s[0] == '+':  # если первый символ +
            s.pop(0)  # удаляем +
            return expr(s)  # вызываем функцию снова
        if s[0] == '-':  # если первый символ -
            s.pop(0)  # удаляем -
            return -(expr(s))  # вызываем отрицательную функцию от этой функции
    return primary(s)  # вызываем следующую функцию


def primary(s: list) -> [int, float]:
    """Функция проверяет, есть ли в списке скобки. Если да, то алгоритм повторяется,
    иначе выводит ответ"""
    if s:
        if '(' in s:  # если есть скобки, переходим снова в функцию expr
            return expr(s)
        return s[0]  # если скобок нет, возвращаем ответ
