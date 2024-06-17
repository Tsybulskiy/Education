import math
from scipy.optimize import fsolve

c = 3 * 10 ** 8
eps_0 = 8.85 * 10 ** (-12)
mu_0 = 4 * math.pi * 10 ** (-7)
E_prob = 3 * 10 ** 6
def calculate_coaxial_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma):


    r = d_max / 2
    print(f"Радиус коаксиальной линии r: {r} м")

    delta = float(input("Введите значение delta: "))

    b = r - delta
    print(f"b: {b}")

    a = b / math.exp((Z_c / 60) * math.sqrt(epsilon))
    print(f"a: {a}")

    L_0 = (mu_0 / (2 * math.pi)) * math.log(b / a)
    print(f"Удельная индуктивность L_0: {L_0} Гн/м")

    C_0 = (2 * math.pi * eps_0 * epsilon) / math.log(b / a)
    print(f"Удельная емкость C_0: {C_0} Ф/м")

    a_pr = (math.sqrt(math.pi * f * mu_0)) / (4 * math.pi * Z_c * math.sqrt(sigma)) * (1 / a + 1 / b)
    print(f"Коэффициент затухания из-за потерь в проводнике a_pr: {a_pr} Нп/м")

    beta = (2 * math.pi * f) / c * math.sqrt(epsilon)
    print(f"Фазовая постоянная beta: {beta} рад/м")

    a_d = beta / 2 * tgdelta
    print(f"Коэффициент затухания из-за диэлектрических потерь a_d: {a_d} Нп/м")

    a_obsh = a_pr + a_d
    print(f"Общий коэффициент затухания a_obsh: {a_obsh} Нп/м")

    A_e = math.exp(a_obsh * l)
    print(f"Амплитуда по мощности A_e: {A_e}")

    A_p = math.exp(2 * a_obsh * l)
    print(f"Амплитуда по мощности и затуханию A_p: {A_p}")

    P_max = (math.pi * a ** 2) / Z_c * math.log(b / a) * E_prob ** 2
    print(f"Предельно допустимая мощность P_max: {P_max} Вт")

    U_max = math.sqrt(Z_c * P_max)
    print(f"Максимально допустимое напряжение U_max: {U_max} В")

    return L_0, C_0, a_obsh, A_e, A_p, P_max, U_max

def calculate_twisted_pair_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma):
    def equations(p):
        D, a = p
        eq1 = D + 2 * a - d_max
        eq2 = Z_c - 120 * math.sqrt(1 / epsilon) * math.log((0.5 * D / a) + math.sqrt((0.5 * D / a) ** 2 - 1))
        return (eq1, eq2)

    D_initial = d_max / 2 + d_max / 4
    a_initial = d_max / 4

    D, a = fsolve(equations, (D_initial, a_initial))

    print(f"D: {D:.6f}, a: {a:.6f}")


    L_0 = mu_0 / math.pi * (math.log(0.5 * D / a + math.sqrt((0.5 * D / a) ** 2 - 1))+ 1 / 4)
    print(f"Удельная индуктивность L_0: {L_0} Гн/м")

    common_log_expr = math.log(0.5 * D / a + math.sqrt((0.5 * D / a) ** 2 - 1))
    C_0 = (math.pi * epsilon * eps_0) / common_log_expr
    print(f"Удельная емкость C_0: {C_0} Ф/м")

    a_pr = 1 / (2 * a * Z_c) * math.sqrt((f * mu_0) / (math.pi * sigma)) * (D / math.sqrt(D ** 2 - 4 * a ** 2))
    print(f"Коэффициент затухания из-за потерь в проводнике a_pr: {a_pr} Нп/м")

    beta = (2 * math.pi * f) / c * math.sqrt(epsilon)
    print(f"Фазовая постоянная beta: {beta} рад/м")

    a_d = beta / 2 * tgdelta
    print(f"Коэффициент затухания из-за диэлектрических потерь a_d: {a_d} Нп/м")

    a_obsh = a_pr + a_d
    print(f"Общий коэффициент затухания a_obsh: {a_obsh} Нп/м")

    A_e = math.exp(a_obsh * l)
    print(f"Амплитуда по мощности A_e: {A_e}")

    A_p = math.exp(2 * a_obsh * l)
    print(f"Амплитуда по мощности и затуханию A_p: {A_p}")

    U_max = a * math.sqrt(2) * math.sqrt((D - 2 * a) / (D + 2 * a)) * math.log(D/a) * E_prob
    print(f"Максимально допустимое напряжение U_max: {U_max} В")

    P_max = U_max ** 2 / Z_c
    print(f"Максимально допустимая мощность P_max: {P_max} Вт")

    return L_0, C_0, a_obsh, A_e, A_p, U_max, P_max


def calculate_symmetrical_stripline(Z_c, epsilon, tgdelta, d_max, l, f, sigma):

    b = d_max
    print(f"b: {b}")


    magic_constant_wow = 0.00165
    multiplier = magic_constant_wow * Z_c * math.sqrt(epsilon)
    w = b * multiplier
    print(f"w: {w} м")


    epsilon_factor = 200 / math.sqrt(epsilon)
    h = fsolve(lambda h: epsilon_factor * ((b - 3 * h) / (2 * w + b - h)) - Z_c, 0.001)[0]

    if h <= 0:
        h = fsolve(lambda h: epsilon_factor * ((b - 3 * h) / (2 * w + b - 3 * h)) - Z_c, 0.001)[0]
        formula_used = 2
    else:
        formula_used = 1

    print(f"h: {h} м")
    print(f"Использованная формула для вычисления h: {formula_used}")


    a_pr = (4.34 * math.sqrt(math.pi * f * mu_0)) / (Z_c * (w + h) * math.sqrt(sigma))
    a_d = (27.3 * math.sqrt(epsilon) * tgdelta * f) / c
    a_obsh = a_pr + a_d

    print(f"Коэффициент затухания из-за проводников a_pr: {a_pr} Нп/м")
    print(f"Коэффициент затухания из-за диэлектрика a_d: {a_d} Нп/м")
    print(f"Общий коэффициент затухания a_obsh: {a_obsh} Нп/м")

    A_e = 10 ** (a_obsh * l / 20)
    A_p = 10 ** (a_obsh * l / 10)
    print(f"Амплитудный коэффициент ослабления A_e: {A_e}")
    print(f"Коэффициент ослабления по мощности A_p: {A_p}")

    return a_obsh, A_e, A_p
def calculate_microstrip_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma):
    b = d_max / 1.1
    h = 0.1 * b
    print(f"Начальные значения: b = {b}, h = {h}")


    epsilon_ef = 0.475 * epsilon + 0.67
    print(f"Эффективная диэлектрическая проницаемость epsilon_ef: {epsilon_ef}")


    def eq1(w):
        return 300 / math.sqrt(epsilon_ef) - Z_c * (1 + w / b - h / b) - (1 - h / b)

    w = fsolve(eq1, 0.001)[0]

    if w <= 0:
        def eq2(w):
            return 300 / math.sqrt(epsilon_ef) - Z_c * (1 + w / b) - (1 - h / b)

        w = fsolve(eq2, 0.001)[0]
        formula_used = 2
    else:
        formula_used = 1

    print(f"Ширина w: {w} м")
    print(f"Использованная формула для вычисления w: {formula_used}")


    a_pr = (4.34 * math.sqrt(math.pi * f * mu_0)) / (Z_c * (w + h) * math.sqrt(sigma))
    a_d = (27.3 * f / c) * tgdelta * ((epsilon_ef - 1) / math.sqrt(epsilon_ef)) * (epsilon / (epsilon - 1))
    a_obsh = a_pr + a_d
    print(f"Коэффициент затухания из-за проводников a_pr: {a_pr} Нп/м")
    print(f"Коэффициент затухания из-за диэлектрика a_d: {a_d} Нп/м")
    print(f"Общий коэффициент затухания a_obsh: {a_obsh} Нп/м")


    A_e = 10**(a_obsh * l / 20)
    A_p = 10**(a_obsh * l / 10)
    print(f"Амплитудный коэффициент ослабления A_e: {A_e}")
    print(f"Коэффициент ослабления по мощности A_p: {A_p}")

    return a_obsh, A_e, A_p
def solve_task5():

    Z_c = float(input("Введите волновое сопротивление Z_c (Ом): "))
    epsilon = float(input("Введите относительную диэлектрическую проницаемость ε: "))
    tgdelta = float(input("Введите тангенс угла потерь tgδ: "))
    d_max = float(input("Введите максимальный диаметр d_max (мм): ")) / 1000
    l = float(input("Введите длину линии l (метры): "))
    f = float(input("Введите частоту f (МГц): ")) * 10 ** 6
    sigma = float(input("Введите проводимость σ (См/м): "))

    print("\n--- Коаксиальная линия ---")
    calculate_coaxial_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma)

    print("\n--- Двухпроводная линия ---")
    calculate_twisted_pair_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma)

    print("\n--- Симметрично-полосовая линия ---")
    calculate_symmetrical_stripline(Z_c, epsilon, tgdelta, d_max, l, f, sigma)

    print("\n--- Микрополосковая линия ---")
    calculate_microstrip_line(Z_c, epsilon, tgdelta, d_max, l, f, sigma)

