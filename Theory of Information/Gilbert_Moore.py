from math import ceil, log2


def gilbert_moore_encoding(frequencies):
    code = {}

    cumulative_prob = 0
    print("\nТаблица Гильберта-Мура:")
    print(
        f"{'Символ':^7} | {'Вероятность pi':^13} | {'Кум. вер. qi':^22} | {'σ i':^5} | {'Дл. кода li':^10} | {'Двоичная запись σ i':^20} | Кодовое слово")

    for char, freq in frequencies.items():
        sigma_i = cumulative_prob + freq / 2
        code_length = ceil(-log2(freq/2))
        sigma_i_rounded = int(sigma_i * 2 ** code_length)
        sigma_bin = format(sigma_i_rounded, f'0{code_length}b')
        code[char] = sigma_bin

        print(f"{char:^7} | {freq:^13.5f} | {cumulative_prob:^22.5f} | {sigma_i:^5.5f} | {code_length:^10} | 0.{sigma_bin.ljust(10, '0')}... | {code[char]}")

        cumulative_prob += freq

    return code