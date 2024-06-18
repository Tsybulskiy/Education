import numpy as np

def get_user_matrix():
    rows = int(input("Введите количество строк в проверочной матрице H: "))
    columns = int(input("Введите количество столбцов в проверочной матрице H: "))
    H = np.zeros((rows, columns), dtype=int)
    for r in range(rows):
        row_input = input(f"Введите строку {r+1} через пробел: ").split()
        if len(row_input) != columns:
            raise ValueError("Неправильное количество элементов в строке.")
        H[r] = [int(x) % 2 for x in row_input]
    return H

def get_user_received_word(columns):
    received_word = input(f"Введите принятое слово длиной {columns} через пробел: ").split()
    if len(received_word) != columns:
        raise ValueError("Неправильная длина принятого слова.")
    return np.array([int(x) % 2 for x in received_word])

def calculate_syndrome(H, r):
    return np.dot(H, r.transpose()) % 2

def find_error_vector(syndrome, H):
    for i, column in enumerate(H.T):
        if np.array_equal(syndrome, column):
            e = np.zeros(H.shape[1], dtype=int)
            e[i] = 1
            return e
    return np.zeros(H.shape[1], dtype=int)

def correct_received_word(r, e):
    return (r + e) % 2


def hamming():
    H = get_user_matrix()
    option = int(input(
        "Выберите решение:\n1) Матрица + полученное сообщение\n2) Матрица + синдром\n3) Матрица + вектор ошибок\nВведите номер опции: "))

    if option == 1:
        r = get_user_received_word(H.shape[1])
        syndrome = calculate_syndrome(H, r)
        error_vector = find_error_vector(syndrome, H)
        corrected_word = correct_received_word(r, error_vector)
    elif option == 2:
        syndrome_elements = input("Введите синдром через пробел: ").split()
        syndrome = np.array([int(x) % 2 for x in syndrome_elements])
        error_vector = find_error_vector(syndrome, H)
        if np.any(error_vector):
            print(f"Вектор ошибки обнаружен: {error_vector}")
            received_word_elements = input(
                f"Введите принятое слово длиной {H.shape[1]} с ошибкой через пробел: ").split()
            r = np.array([int(x) % 2 for x in received_word_elements])
            corrected_word = correct_received_word(r, error_vector)
        else:
            r = corrected_word = None
            print("Не найдена одиночная ошибка с этим синдромом.")
    elif option == 3:
        error_vector_elements = input("Введите вектор ошибок через пробел: ").split()
        error_vector = np.array([int(x) % 2 for x in error_vector_elements])
        syndrome = calculate_syndrome(H, error_vector)
        received_word_elements = input(f"Введите принятое слово длиной {H.shape[1]} через пробел: ").split()
        if len(received_word_elements) != H.shape[1]:
            raise ValueError("Неправильная длина принятого слова.")
        r = np.array([int(x) % 2 for x in received_word_elements])
        corrected_word = correct_received_word(r, error_vector)
    else:
        raise ValueError("Неверный номер опции!")
    if corrected_word is None:
        r = syndrome = error_vector = np.full(H.shape[1], None)
    if r is not None:
        corrected_word = correct_received_word(r, error_vector)
    else:
        corrected_word = None
    print(f"Полученное сообщение: {r}")
    print(f"Синдром: {syndrome}")
    print(f"Вектор ошибок: {error_vector}")
    print(f"Исправленное принятое слово (без проверочных битов): {corrected_word}")



