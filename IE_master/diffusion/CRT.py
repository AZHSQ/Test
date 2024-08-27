

def chinese_remainder_theorem(moduli, remainders):
    if len(moduli) != len(remainders):
        raise ValueError("The number of moduli and remainders must be the same.")
    M = 1
    for m in moduli:
        M *= m
    result = 0
    for i in range(len(moduli)):
        mi = M // moduli[i]
        yi = pow(mi, -1, moduli[i])
        result += remainders[i] * mi * yi
    return result % M

def compute_remainders(result, moduli):
    remainders = []
    M = 1
    for m in moduli:
        M *= m
    for m in moduli:
        Mi = M // m
        yi = pow(Mi, -1, m)
        remainder = (result * Mi * yi) % m
        remainders.append(remainder)
    return remainders
