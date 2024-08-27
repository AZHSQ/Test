import math
from operator import mod
from math import cos, pi, sin, exp
import numpy as np
from scipy.linalg import hadamard

from chaos.chaos_generator import generate_chaos_sequence




def hadamard_matrix(x0, y0, p1, p2, CR, length):
    chaos_seq_x, chaos_seq_y, chao_seq_w, chaos_seq_z = generate_chaos_sequence(x0, y0, p1, p2, 1, length)
    result = []
    for i in range(len(chaos_seq_x)):
        element = (chaos_seq_x[i] + chaos_seq_z[i]) / 2
        result.append(element)
    result = [mod(math.floor(element * 10 ** 9), length) for element in result]

    phi1_indices = np.argsort(result)
    had_src = hadamard(length).astype(np.float32)

    phi1 = had_src[phi1_indices[:int((CR * length))], :]
    return phi1





