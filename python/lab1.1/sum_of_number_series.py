import math
import Series as sc

def f1(k):
    return 1 / (2*k + 1)**2

def f2(k):
    return (-1)**k / (2*k + 1)**3

def f1V(x):
    """
    Функція f1(x) = (-1)^x/x(3x+2)
    """
    return (-1)**x / (x * (3 * x + 2))
def f2V(x):
    """
    Функція f(x) = 1 / (x(3x+2))
    """
    return 1 / (x * (3 * x + 2))

def test_series():
    results = []

    result1 = sc.SeriesCalculator.sum_finite(f2V, 1, 15100)
    results.append(("Сума 1 / (k(3k+2)) від k=1 до 15100:", result1))

    result5, terms5 = sc.SeriesCalculator.series_sum_with_tolerance_infinite(f1V, epsilon=10**-9, max_iter=10**7)
    results.append(("Сума ряду (-1)^x/x(3x+2) з урахуванням похибки", result5))
    exact = 3/4 * (1 - 2*math.pi / 27**0.5)
    results.append(("Точне значення 3/4(1-2π/27^0.5)", exact))
    results.append(("Кількість використаних членів", terms5))
    results.append(("Модуль різниці точного і обчисленого значень", abs(result5 - exact)))

    with open("python/lab1.1/Gavinskii_Timofiy.txt", "w", encoding="utf-8") as file:
        for name, val in results:
            file.write(f"{name}: {val:.10f}\n")
    print(" Результати збережено у файл Gavinskii_Timofiy.txt")


    results_EX = []
    # --- Приклад 1: сума 1/(2k+1)^2 від k=1 до 10000 ---
    result1 = sc.SeriesCalculator.sum_finite(f1, 1, 10000)
    exact1 = math.pi**2 / 8 - 1
    results_EX.append(("Сума 1/(2k+1)^2 від 1 до 10000: \n\t 1. ", result1))
    results_EX.append(("\t 2. ", exact1))

    # --- Приклад 2: знакозмінний ряд (-1)^k / (2k+1)^3 ---
    result2 = sc.SeriesCalculator.sum_finite(f2, 0, 10000)
    exact2 = math.pi**3 / 32
    results_EX.append(("Сума (-1)^k/(2k+1)^3 від 0 до 10000: \n\t 1. ", result2))
    results_EX.append(("\t 2. ", exact2))

    # --- Приклад 3: нескінченний ряд сума 1/(2k+1)^2, відомо що -> π^2/6 ---
    result3, terms3 = sc.SeriesCalculator.sum_infinite(f1, start=0, eps=1e-9)
    exact3 = math.pi**2 / 8 - 1
    results_EX .append(("\n Нескінченний ряд сума 1/(2k+1)^2", result3))
    results_EX.append(("Точне значення (π^2/8)-1", exact3))
    results_EX.append(("Кількість використаних членів", terms3))

    # --- Приклад 4: нескінченний знакозмінний ряд ---
    result4, terms4 = sc.SeriesCalculator.sum_infinite(f2, start=0, eps=1e-9)
    exact4 = math.pi**3 / 32
    results_EX.append(("\n Нескінченний ряд (-1)^k/(2k+1)^3", result4))
    results_EX.append(("Точне значення π^3/32", exact4))
    results_EX.append(("Кількість використаних членів", terms4))

    # --- Приклад 5: Використання series_sum_with_tolerance ---
    result5, terms5 = sc.SeriesCalculator.series_sum_with_tolerance(f1, epsilon=1e-6)
    results_EX.append(("\n Сума ряду 1/(2k+1)^2 з урахуванням похибки", result5))
    results_EX.append(("Кількість використаних членів", terms5))

    # --- Приклад 6: Використання series_sum_with_tolerance ---
    result6, terms6 = sc.SeriesCalculator.series_sum_with_tolerance(f2, epsilon=1e-6)
    results_EX.append(("\n Сума ряду (-1)^k/(2k+1)^3 з урахуванням похибки", result6))
    results_EX.append(("Кількість використаних членів", terms6))

    with open("python/lab1.1/lab2_results.txt", "w", encoding="utf-8") as f:
        for name, val in results_EX:
            f.write(f"{name}: {val:.10f}\n")

    print("Результати збережено у файл lab2_results.txt")