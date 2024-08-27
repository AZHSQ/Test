import math
import os
import random
from operator import mod, xor
import time
import cv2
import numpy as np
from chaos.chaos_generator import generate_chaos_sequence
from diffusion.complementary import complementary_list
from encryption.process import int_to_binary_string, dna_encryption
from encryption.dna_calc import dna_xor
from encryption.dna_coding import encode_to_dna, decode_dna_to_binary


def encryption(img, x0, y0, m, n, Joseph_iterations, c1, c2, c3, c4):
    np.set_printoptions(threshold=np.inf)

    row, col = np.array(img).shape
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

    img = img.reshape((image_size))
    dna_image_list = []

    for i in range(image_size):
        dna_image_list.append(dna_encryption(img[i], dna_enRule[i], joseph_Traversal_iteration[i]))
    bin_key_seq = []
    for i in range(image_size):
        bin_key_seq.append(int_to_binary_string(seq_x[i]))

    dna_key = []
    for j in range(len(bin_key_seq)):
        dna_key.append(encode_to_dna(bin_key_seq[j], dna_enRule[j]))
    ciper = []
    for i in range(len(dna_key)):
        if i == 0:
            ciper.append(dna_xor(dna_image_list[i], dna_key[i]))
        else:
            ciper.append(dna_xor(dna_image_list[i], dna_xor(dna_key[i], ciper[i - 1])))
    dna_list = ciper

    res = []
    for i in range(len(dna_list)):
        res.append(complementary_list(dna_list[i], complementary_rule[i],
                                      complementary_iteration[i], c1, c2, c3, c4))

    image_decoding = []
    for i in range(image_size):
        binary_seq = decode_dna_to_binary(res[i], dna_deRule[i])
        image_decoding.append(int(binary_seq, 2))
    img_encryption = np.array(image_decoding).reshape(row, col)

    return img_encryption
