import time
import random
import poly_logic as pl
import mult_methods as mm


def benchmark_mult():
    # Длины массивов для тестов
    sizes = [16, 32, 64, 128, 256, 512, 1024]

    print(f"{'Размер':<8} {'Обычное (с)':<15} {'Карацуба (с)':<15} | {'Разница в ':<15}")
    print()

    for n in sizes:
        # Генерим случайные многочлены
        p1 = [random.randint(0, 100) for _ in range(n)]
        p2 = [random.randint(0, 100) for _ in range(n)]

        # Замер классики
        t_start = time.time()
        mm.simple_mult(p1, p2)
        t_simple = time.time() - t_start

        # Замер Карацубы
        t_start = time.time()
        mm.karatsuba(p1, p2)
        t_kara = time.time() - t_start

        # Разница
        if 0 not in [t_simple, t_kara]:
            diff = max(t_simple, t_kara) / min(t_simple, t_kara)
        else:
            diff = 1

        print(f"{n:<8} {t_simple:<15.6f} {t_kara:<15.6f} {diff:<15.6f}")


def benchmark_horner():
    print("\nСравнение Горнера и прямого расчета")
    n = 50000  # Степень многочлена
    poly = [random.random() for _ in range(n)]
    x = 1.0001

    t1 = time.time()
    res1 = pl.calc_direct(poly, x)
    elapsed1 = time.time() - t1

    t2 = time.time()
    res2 = pl.calc_horner(poly, x)
    elapsed2 = time.time() - t2

    print(f"Прямой метод (N={n}): {elapsed1:.6f} сек")
    print(f"Схема Горнера (N={n}): {elapsed2:.6f} сек")
    print(f"Разница: в {elapsed1 / elapsed2:.1f} раз")


if __name__ == "__main__":
    benchmark_mult()
    benchmark_horner()