from markov_equation import solve_modified_system
from collections import defaultdict
from math import log2
from Shannon import shannon_encoding
from Huffman import build_tree, huffman_encoding
from Gilbert_Moore import gilbert_moore_encoding
from Arithmetic import arithmetic_encoding
from entropy_and_self_information_for_1 import self_information, symbol_entropy
from conditional_entropy import calculate_joint_probabilities, marginal_probabilities, conditional_entropy, \
    joint_entropy
from markov_chains import multiply_matrices
from hamming_code import hamming
from Speed_coding import spead


def entropy(frequencies, total):
    return -sum((freq / total) * log2(freq / total) for freq in frequencies.values())


def average_code_length(frequencies, code):
    return sum(len(code[char]) * freq for char, freq in frequencies.items())


from collections import defaultdict

def get_frequencies(n):
    frequencies = defaultdict(int)
    for i in range(n):
        char, prob = input(f"Введите символ и его вероятность (через пробел) для символа {i + 1}: ").split()
        frequencies[char] = float(prob)
    return frequencies

def display_codes(code, title):
    print(f"\n{title}:")
    for char, code_str in code.items():
        print(f"{char}: {code_str}")


def handle_method_6(rows, columns):
    joint_probabilities = calculate_joint_probabilities(rows, columns)
    row_sums = marginal_probabilities(joint_probabilities, 'row')
    column_sums = marginal_probabilities(joint_probabilities, 'column')

    total_row_sum = sum(row_sums)
    total_column_sum = sum(column_sums)

    H_X = entropy(dict(enumerate(row_sums)), total_row_sum)
    H_Y = entropy(dict(enumerate(column_sums)), total_column_sum)
    H_joint = joint_entropy(joint_probabilities)
    H_X_given_Y = conditional_entropy(H_joint, H_Y)
    H_Y_given_X = conditional_entropy(H_joint, H_X)

    print("Суммы строк и столбцов:")
    for i, row_sum in enumerate(row_sums):
        print(f"Строка {i + 1}: {row_sum}")
    for i, column_sum in enumerate(column_sums):
        print(f"Столбец {i + 1}: {column_sum}")

    print(f"\nЭнтропия H(X): {H_X}")
    print(f"Энтропия H(Y): {H_Y}")
    print(f"Взаимная энтропия H(X;Y): {H_joint}")
    print(f"Условная энтропия H(X|Y): {H_X_given_Y}")
    print(f"Условная энтропия H(Y|X): {H_Y_given_X}")

def main():
    method = input(
        "Выберите задачу (1 - Кодирование алгоритмом Хаффмана, 2 - Кодирование алгоритмом Шеннона, 3- Кодирвоание алгоритмом Гильберта-Мура, 4-Арифметическоt кодирование, 5- Энтропия и "
        "собственная информация одного источника 6-Условная энтропия, 7-Марковские цепи, 8-Марковские цепи решение уравнения, "
        "9-Скорость кодирование, 10-Кодирование алгоритмом Хэмминга): ")

    if method in ["1", "2", "3", "4", "5"]:
        n = int(input("Введите количество символов: "))
        frequencies = get_frequencies(n)

    if method == "1":
        root = build_tree(frequencies)
        code = huffman_encoding(root)
        display_codes(code, "Код Хаффмана")
    elif method == "2":
        code = shannon_encoding(frequencies)
        display_codes(code, "Код Шеннона")
    elif method == "3":
        code = gilbert_moore_encoding(frequencies)
        display_codes(code, "Код Гильберта-Мура")
    elif method == "4":
        sequence = input("Введите последовательность символов для кодирования: ")
        arithmetic_code = arithmetic_encoding(frequencies, sequence)
        print('Пример: q(bcaa)=q(bca)+p(bca)*q(a)')
        print('p(bcaa)=p(bca)*p(a) и т.д по рекурсии')
        print('l(bcaa)=⌈-log_2(p(bcaa))⌉+1')
        print('σ i(bcaa)=q(bcaa)+1/2*p(bcaa)')
    elif method == "5":
        total_symbols = sum(frequencies.values())
        symbols_entr = symbol_entropy(frequencies)
        symbols_info = self_information(frequencies)
        print("\nЭнтропия каждого символа:")
        for char, entropy_value in symbols_entr.items():
            print(f"{char}: {entropy_value}")
        print("\nСобственная информация каждого символа:")
        for char, info_value in symbols_info.items():
            print(f"{char}: {info_value}")
        print("\nДля энтропии H=p*I Для собственной информации I=-log_2(p)")
    elif method == "6":
        rows = int(input("Введите количество строк: "))
        columns = int(input("Введите количество столбцов: "))
        handle_method_6(rows, columns)
    elif method == "7":
        multiply_matrices()
    elif method == "8":
        print("Очень важно что матрицу нужно вводить так, как вы строите уравнение, то есть столбцы=строки")
        solve_modified_system()
    elif method == "9":
        N = int(input("Введите N: "))
        n = int(input("Введите n: "))
        x = int(input("Введите x: "))
        print(spead(N, n, x))
    elif method == "10":
        hamming()

    try:
        total_symbols = sum(frequencies.values())
        entr = entropy(frequencies, total_symbols)
        average_len = average_code_length(frequencies, code)
        redundancy = average_len - entr
        print(f"\nЭнтропия источника H: {entr}")
        print(f"Средняя длина кода l: {average_len}")
        print(f"Избыточность кода r, r=l-H: {redundancy}")
    except:
        pass

if __name__ == "__main__":
    main()
