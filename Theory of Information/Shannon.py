from math import ceil, log2


def shannon_encoding(frequencies):
    code = {}
    sorted_freq = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)

    cumulative_prob = 0
    print("\nТаблица Шеннона:")
    print(f"{'Символ':^7} | {'Вероятность pi':^13} | {'Кум. вер qi.':^10} | {'Дл. кода li':^9} | {'Кум. вер. (бин)':^15} | Кодовое слово")

    for i, (char, freq) in enumerate(sorted_freq):
        code_length = ceil(-log2(freq))
        cumulative_bin = format(int(cumulative_prob * 2**code_length), f'0{code_length}b')
        code[char] = cumulative_bin

        print(f"{char:^7} | {freq:^13.5f} | {cumulative_prob:^10.5f} | {code_length:^9} | 0.{cumulative_bin.ljust(10, '0')}... | {code[char]}")

        cumulative_prob += freq

    return code