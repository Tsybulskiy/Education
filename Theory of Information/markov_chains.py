import numpy as np

def enter_matrix(prompt):
    print(prompt)
    rows = int(input("Введите количество строк матрицы: "))
    cols = int(input("Введите количество столбцов матрицы: "))
    matrix = []
    for i in range(rows):
        row_input = input(f"Введите элементы строки {i+1} через пробел: ")
        row = list(map(float, row_input.split()))
        assert len(row) == cols, "Количество элементов в строке не соответствует заявленному количеству столбцов."
        matrix.append(row)
    return np.array(matrix)

def multiply_matrices():
    matrix_a = enter_matrix("Введите значения первой матрицы (A):")

    matrix_b = enter_matrix("Введите значения второй матрицы (B):")

    num_multiplications = int(input("Введите количество перемножений матрицы B на A: "))

    for i in range(num_multiplications):
        result_matrix = np.dot(matrix_b, matrix_a)
        print(f"Результат умножения после {i+1} итерации:")
        print(result_matrix)
        matrix_b = result_matrix

