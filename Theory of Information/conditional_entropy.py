from math import log2, isclose


def calculate_joint_probabilities(rows, columns):
    joint_probabilities = []
    for i in range(rows):
        row_probabilities = list(map(float, input(f"Введите вероятности для строки {i + 1}. Введите {columns} числа через пробел: ").split()))
        assert len(row_probabilities) == columns, f"В строке {i + 1} должно быть {columns} вероятностей."
        joint_probabilities.append(row_probabilities)
    return joint_probabilities

def marginal_probabilities(joint_probabilities, orientation):
    if orientation == 'row':
        return [sum(row) for row in joint_probabilities]
    elif orientation == 'column':
        return [sum(column[i] for column in joint_probabilities) for i in range(len(joint_probabilities[0]))]

def conditional_entropy(H_joint, H_marginal):
    if isclose(H_joint, 0.0) or isclose(H_marginal, 0.0):
        return float('nan')
    return H_joint - H_marginal
def joint_entropy(joint_probabilities):
    entropy = 0
    for row in joint_probabilities:
        for prob in row:
            if prob > 0:
                entropy += prob * log2(prob)
    return -entropy
