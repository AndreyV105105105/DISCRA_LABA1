# Базовые операции с многочленами (массивами коэффициентов)

def calc_direct(poly, x):
    """Считаем значение по обычному : a0*x^0 + a1*x^1.."""
    res = 0
    for i in range(len(poly)):
        res += poly[i] * (x ** i)
    return res

def calc_horner(poly, x):
    """Схема Горнера"""
    res = 0
    # Идем с конца массива к началу
    for i in range(len(poly) - 1, -1, -1):
        res = res * x + poly[i]
    return res

def add_p(p1, p2):
    """Простое сложение двух списков разной длины"""
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(n):
        v1 = p1[i] if i < len(p1) else 0
        v2 = p2[i] if i < len(p2) else 0
        res[i] = v1 + v2
    return res

def sub_p(p1, p2):
    """Вычитание списков (нужно для Карацубы)"""
    n = max(len(p1), len(p2))
    res = [0] * n
    for i in range(n):
        v1 = p1[i] if i < len(p1) else 0
        v2 = p2[i] if i < len(p2) else 0
        res[i] = v1 - v2
    return res