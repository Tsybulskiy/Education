from math import log2


def self_information(frequencies):
    return {char: -log2(freq) for char, freq in frequencies.items()}

def symbol_entropy(frequencies):
    info = self_information(frequencies)

    return {char: info[char] * freq for char, freq in frequencies.items()}
