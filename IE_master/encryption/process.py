
import numpy as np

from JT.JT import joseph_sequence


from encryption.dna_coding import encode_to_dna

def int_to_binary(n):
    binary_str = bin(n)[2:]
    binary_str = '0' * (8 - len(binary_str)) + binary_str
    return binary_str


def binary_to_matrix(binary_str):
    matrix = np.zeros((3, 3))
    row = 3
    col = 3
    q = 0
    for i in range(row):
        for j in range(col):
            if i == 0 and j == 0:
                continue
            matrix[i][j] = int(binary_str[q])
            q = (q + 1) % (row * col)
    matrix[0][0] = -1
    return matrix


def arnold_encode(matrix, a, b, iterations):
    width = len(matrix)
    height = len(matrix[0])
    N = len(matrix[0])
    for _ in range(iterations):
        new_matrix = [[0] * N for _ in range(N)]
        for x in range(width):
            for y in range(height):
                new_x = (x + b * y) % N
                new_y = ((a * x) + (a * b * y) + y) % N
                new_matrix[new_x][new_y] = matrix[x][y]
        matrix = new_matrix
    return matrix


def matrix_to_binary(matrix):
    binlist = np.zeros(8)
    row = len(matrix)
    col = len(matrix[0])
    q = 0
    for i in range(row):
        for j in range(col):
            if matrix[i][j] == -1:
                continue
            binlist[q] = matrix[i][j]
            q = (q + 1) % (row * col)
    return binlist


def dna_encryption(integer_value, releNumber, iterations):
    list = []
    binary_sequence = int_to_binary(integer_value)
    result_string = joseph_sequence(binary_sequence, 1, iterations)
    for i in range(len(result_string)):
        list.append(int(result_string.tolist()[i]))
    binary_str = ''.join(map(str, list))

    dna_sequence = encode_to_dna(binary_str, releNumber)

    return dna_sequence


def int_to_binary_string(number):
    binary_str = bin(number)[2:]
    if (len(binary_str) != 8):
        padding_zeros = 8 - len(binary_str) % 8
        binary_str = '0' * padding_zeros + binary_str
    return binary_str
