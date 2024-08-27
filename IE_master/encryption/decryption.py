import cv2
import numpy as np
from operator import mod
from chaos.chaos_generator import generate_chaos_sequence
from diffusion.complementary import reverse_complementary
from encryption.process import int_to_binary, int_to_binary_string
from encryption.dna_calc import dna_xor
from encryption.dna_coding import encode_to_dna, decode_dna_to_binary
import math

from JT.JT import reverse_joseph_sequence


def pixel_into_dna(integer_value, ruleNumber):
    binary_str = int_to_binary(integer_value)
    dna_sequence = encode_to_dna(binary_str, ruleNumber)
    return dna_sequence


def de_encryption(binary_seq, iterations):
    list = []
    result_string = reverse_joseph_sequence(binary_seq, 1, iterations)

    for i in range(len(result_string)):
        list.append(int(result_string.tolist()[i]))
    binary_str = ''.join(map(str, list))
    decimal_integer = int(binary_str, 2)
    return decimal_integer


def de_encryption_func(en_img, x0, y0, m, n, Joseph_iterations, c1, c2, c3, c4):

    row, col = en_img.shape
    image_size = row * col

    chaos_seq_x, chaos_seq_y, chaos_seq_w, chaos_seq_z = generate_chaos_sequence(x0, y0, m, n, row, col)
    dna_enRule = [mod(math.floor(element * 10 ** 18), 8) for element in chaos_seq_x]
    dna_deRule = [mod(math.floor(element * 10 ** 18), 8) for element in chaos_seq_y]
    joseph_Traversal_iteration = []
    seq_x = [mod(math.floor(element * 10 ** 18), 256) for element in chaos_seq_x]
    seq_z = [mod(math.floor(element * 10 ** 18), 256) for element in chaos_seq_z]
    for i in range(image_size):
        joseph_Traversal_iteration.append(mod(seq_x[i] ^ seq_z[i], Joseph_iterations))

    complementary_rule = [math.floor(element * 10 ** 18) for element in chaos_seq_w]
    complementary_iteration = [math.floor(element * 10 ** 18) for element in chaos_seq_z]
    length = row * col
    image_de1 = []
    image_1d = en_img.reshape(length)
    for i in range(row * col):
        image_de1.append(pixel_into_dna(image_1d[i], dna_deRule[i]))
    complementary_list = []
    for i in range(length):
        complementary_list.append(
            reverse_complementary(image_de1[i], complementary_rule[i], complementary_iteration[i], c1, c2, c3, c4))  # 求逆补集规则
    ciper = []
    bin_key_seq = []
    for i in range(len(seq_x)):
        bin_key_seq.append(int_to_binary_string(seq_x[i]))

    dna_key = []
    for j in range(len(bin_key_seq)):
        dna_key.append(encode_to_dna(bin_key_seq[j], dna_enRule[j]))
    for i in range(len(dna_key)):
        if i == 0:
            ciper.append(dna_xor(complementary_list[i], dna_key[i]))
        else:
            ciper.append(dna_xor(complementary_list[i], dna_xor(dna_key[i], complementary_list[i - 1])))


    image_de2 = []
    for i in range(length):
        image_de2.append(decode_dna_to_binary(ciper[i], dna_enRule[i]))

    image_de3 = []
    for i in range(length):
        image_de3.append(de_encryption(image_de2[i], joseph_Traversal_iteration[i]))

    image_de_final = np.array(image_de3).reshape(row, col)
    return image_de_final
