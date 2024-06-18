import math
from scipy.optimize import fsolve

# Предположим, что значения Z_c и epsilon уже определены ранее в коде
Z_c=150
epsilon=7
b = 0.025
print(f"b: {b}")

magic_constant_wow = 0.00165
multiplier = magic_constant_wow * Z_c * math.sqrt(epsilon)
w = b * multiplier
print(f"w: {w} м")

epsilon_factor = 200 / math.sqrt(epsilon)


def solve_for_h(initial_guess):
    return fsolve(lambda h: epsilon_factor * ((b - 3 * h) / (2 * w + b - h)) - Z_c, initial_guess)[0]


def find_valid_h(initial_guess):
    h = solve_for_h(initial_guess)
    if 0 < h < 1:
        return h, 1
    formula_used = 1

    h = fsolve(lambda h: epsilon_factor * ((b - 3 * h) / (2 * w + b - 3 * h)) - Z_c, initial_guess)[0]
    if 0 < h < 1:
        return h, 2
    formula_used = 2

    return None, formula_used


initial_guess = 0.1
while initial_guess >= 1e-10:
    h, formula_used = find_valid_h(initial_guess)
    if h:
        break
    initial_guess /= 10

if not h:
    raise ValueError("Не удалось найти подходящее h в пределах [0, 1]")

print(f"h: {h} м")
print(f"Использованная формула для вычисления h: {formula_used}")
