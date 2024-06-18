from fractions import Fraction
import numpy as np

def input_matrix(size):
    A = np.zeros((size, size))
    print(f"Введите элементы матрицы {size}x{size} построчно:")
    for i in range(size):
        row = input(f"Строка {i+1}: ").split()
        A[i] = list(map(float, row))
    return A

def number_to_string(num, precision=12):
    return format(num, f".{precision}f").rstrip('0').rstrip('.')

def solve_modified_system():
    size = int(input("Введите размер квадратной матрицы: "))
    A = input_matrix(size)
    A -= np.eye(size)
    B = np.zeros(size)
    A = np.vstack([A, np.ones(size)])
    B = np.append(B, 1)

    try:
        solution, residuals, rank, s = np.linalg.lstsq(A, B, rcond=None)
        print("Решение системы уравнений:")
        for i in range(size):
            float_sol = solution[i]
            frac = Fraction.from_float(float_sol).limit_denominator()
            num_str = number_to_string(float_sol)
            print(f"x{i + 1} = {num_str} ≈ {frac}")
    except np.linalg.LinAlgError as e:
        print("Система уравнений не имеет единственного решения.", e)