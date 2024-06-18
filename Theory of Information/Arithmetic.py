from math import ceil, log2


def arithmetic_encoding(frequencies, sequence):
    intervals = {}
    low = 0
    for char, freq in frequencies.items():
        intervals[char] = (low, low + freq)
        low += freq

    def find_code(low, high, depth, cumulative_sequence=''):
        if depth == len(sequence):
            code = (low + high) / 2
            probability = high - low
            code_length = ceil(-log2(probability)) + 1
            binary_result = format(int(code * (2**code_length)), '0{}b'.format(code_length))
            print(f"σ i: {code:.6f}")
            print(f"Двоичный вид σ i: {binary_result} (Длина кода l: {code_length})")
            return code
        char = sequence[depth]
        cumulative_sequence += char
        char_low, char_high = intervals[char]
        new_low = low + (high - low) * char_low
        new_high = low + (high - low) * char_high

        print(f"Step {depth+1}: char = '{cumulative_sequence}', q({cumulative_sequence}) = {new_low:.6f}, p({cumulative_sequence}) = {new_high-new_low:.6f}")
        return find_code(new_low, new_high, depth + 1, cumulative_sequence)

    return find_code(0, 1, 0)