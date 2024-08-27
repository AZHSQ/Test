import hashlib
import random
from math import floor
from operator import xor, mod

import cv2
import numpy as np

def BinaryGenerator(binary_sequence):

    split_parts = [binary_sequence[i:i + 8] for i in range(0, len(binary_sequence), 8)]
    for i, part in enumerate(split_parts):
        split_parts_list = [binary_sequence[i:i + 8] for i in range(0, len(binary_sequence), 8)]
    return split_parts_list


def xor_between_numbers(num_list_new, start, end):
    result = num_list_new[start]
    for num in range(start + 1, end):
        result = xor(result, num_list_new[num])
    return result


def sum_between_numbers(num_list_new, start, end):
    result = num_list_new[start]
    for num in range(start + 1, end):
        result += num_list_new[num]
    return result


def max_between_number(num_list_new, start, end):
    max_value = np.max(num_list_new[start:end])
    return max_value


def secret_key_generator(image, t0, t1, t2, t3):

    k = []

    hex_number = hashlib.sha512(image).hexdigest()

    binary_number = bin(int(hex_number, 16))[2:]
    if len(binary_number) < 512:
        padding_length = 512 - len(binary_number)
        binary_number = "0" * padding_length + binary_number
    binary_list = BinaryGenerator(binary_number)
    binary_list = [int(element, 2) for element in binary_list]

    k0 = (xor_between_numbers(binary_list, 0, 8) + xor_between_numbers(binary_list, 56, 64)) / (2 * 256) * t0 * t3

    k1 = (binary_list[8] + xor_between_numbers(binary_list, 9, 16) + (xor_between_numbers(binary_list, 48, 56) / 256) + t1) / (3 * 256) * t2

    k2 = (xor_between_numbers(binary_list, 16, 24) + t2 + xor_between_numbers(binary_list, 24, 31) + (binary_list[32]) * t3) / (3 * 256)

    k3 = max_between_number(binary_list, 32, 40) / sum_between_numbers(binary_list, 32, 40) * t0 * t2

    k4 = max_between_number(binary_list, 40, 48) / sum_between_numbers(binary_list, 40, 48) * t1 * t3

    x0 = float(('%.10f' % (mod(floor((k0 + k1 + k2) * pow(10, 10)) * t0, 512) / 512)))
    y0 = float(('%.10f' % (mod(floor((k2 + k3 + k4) * pow(10, 10)) * t1, 512) / 512)))
    m = float(('%.10f' % (mod(floor((k4 + k1 + k2) * pow(10, 7)) * t2, 10) + 20)))
    n = float(('%.10f' % (mod(floor((k0 + k1 + k2 + k3 + k4) * pow(10, 7)) * t3, 10) + 20)))

    Joseph_iterations = floor(mod((k0 + k1 + k2 + k3 + t0 + t3) * pow(10, 10), 8) + 1)

    a = floor(mod((k0 + t1) * pow(10, 10), 64))
    b = floor(mod((k2 + k3) * pow(10, 10), 64))
    arnold_iterations = floor(mod((k3 + k4) * pow(10, 10), 64) + 10)
    return x0, y0, m, n,  Joseph_iterations, a, b, arnold_iterations


