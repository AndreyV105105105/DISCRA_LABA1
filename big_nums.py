from mult_methods import karatsuba, simple_mult


def str_to_poly(s):
    """Превращаем строку '123' в массив коэффициентов [3, 2, 1]"""
    return [int(char) for char in s[::-1]]


def poly_to_str(poly):
    """Собираем число обратно из массива, учитывая переносы разряда"""
    res_val = 0
    for i, coeff in enumerate(poly):
        res_val += coeff * (10 ** i)
    return str(res_val)


def mult_strings(s1, s2, fast=True):
    """Умножение чисел в виде строк"""
    p1 = str_to_poly(s1)
    p2 = str_to_poly(s2)

    if fast:
        res_p = karatsuba(p1, p2)
    else:
        res_p = simple_mult(p1, p2)

    return poly_to_str(res_p)