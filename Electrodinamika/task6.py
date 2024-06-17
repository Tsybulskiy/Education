import math
import cmath
c = 3 * 10 ** 8
def solve_task6():
    def calculate_reflection(Z_n, Z_c):
        return (Z_n - Z_c) / (Z_n + Z_c)

    def calculate_transmission(Z_n, Z_c):
        return (2 * cmath.sqrt(Z_n * Z_c)) / (Z_n + Z_c)


    def solve():

        R_n = float(input("Введите активное сопротивление нагрузки R_n (Ом): "))
        X_n = float(input("Введите реактивное сопротивление нагрузки X_n (Ом): "))
        f = float(input("Введите частоту f (МГц): ")) * 10**6
        Z_c = float(input("Введите волновое сопротивление Z_c (Ом): "))

        Z_n = complex(R_n, X_n)
        print(f"Сопротивление нагрузки Z_n: {Z_n}")

        G = calculate_reflection(Z_n, Z_c)
        G_abs = abs(G)
        print(f"Коэффициент отражения G: {G}")
        print(f"Модуль коэффициента отражения |G|: {G_abs}")

        T = calculate_transmission(Z_n, Z_c)
        print(f"Коэффициент прохождения T: {T}")

        KSV = (1 + G_abs) / (1 - G_abs)
        KBV = (1 - G_abs) / (1 + G_abs)
        print(f"Коэффициент стоячей волны KSV: {KSV}")
        print(f"Коэффициент бегущей волны KBV: {KBV}")

        P_otr = G_abs ** 2
        P_prosh = 1 - P_otr
        print(f"Относительный уровень мощности отраженной волны P_otr: {P_otr}")
        print(f"Относительный уровень мощности прошедшей волны P_prosh: {P_prosh}")

        wavelength = c / f
        print(f"Длина волны: {wavelength} м")

        Z_t = cmath.sqrt(Z_n * Z_c)
        print(f"Сопротивление трансформатора Z_t: {Z_t}")
        print(f"Модуль  преобразователя |Z_t|: {abs(Z_t)}")
        Z_nn = Z_n / Z_c
        Y_nn = 1 / Z_nn
        print(f"Нормированное сопротивление нагрузки Z_nn: {Z_nn}")
        print(f"Нормированная проводимость Y_nn: {Y_nn}")

    solve()