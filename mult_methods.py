import poly_logic as pl


def simple_mult(p1, p2):
    """Классика O(n^2)."""
    n, m = len(p1), len(p2)
    res = [0] * (n + m - 1)
    for i in range(n):
        if p1[i] == 0: continue  # Оптимизация для нулей
        for j in range(m):
            res[i + j] += p1[i] * p2[j]
    return res


def karatsuba(p1, p2):
    """Умножение Карацубы O(n^1.54)."""
    n = max(len(p1), len(p2))

    # Если многочлены маленькие, умножаем классикой, Вы на семе говорили, что Карацуба нужна для больших чисел
    if n <= 32:
        return simple_mult(p1, p2)

    k = n // 2

    # Делим пополам
    low1, high1 = p1[:k], p1[k:]
    low2, high2 = p2[:k], p2[k:]


    z0 = karatsuba(low1, low2)
    z2 = karatsuba(high1, high2)

    # Считаем среднюю часть
    s1 = pl.add_p(low1, high1)
    s2 = pl.add_p(low2, high2)
    z1 = karatsuba(s1, s2)
    z1 = pl.sub_p(z1, pl.add_p(z0, z2))

    # Собираем все в один массив со сдвигами
    res = [0] * (2 * n)
    for i, v in enumerate(z0): res[i] += v
    for i, v in enumerate(z1): res[i + k] += v
    for i, v in enumerate(z2): res[i + 2 * k] += v

    # Чистим нули в конце
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res