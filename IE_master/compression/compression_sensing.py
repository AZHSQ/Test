import cv2
import numpy as np


from SL0 import SL0
from compression.arnold import arnold_encode, arnold_decode
from measure_matrix.hadamard import hadamard_matrix


def compresssion_func(imagepath, x0, y0, p1, p2, CR, a, b, arnold_iterations):
    image = cv2.imread(imagepath, 0)
    m, n = image.shape
    img = image.astype(np.float32)
    image_dct = cv2.dct(img)
    image_dct = arnold_encode(image_dct, a, b, arnold_iterations)
    hadamard_phi = hadamard_matrix(x0, y0, p1, p2, CR, m)
    image_compressed = hadamard_phi.dot(image_dct)
    max_value = np.max(image_compressed)
    min_value = np.min(image_compressed)
    image_compressed_row = int(CR * m)
    image_compressed_col = n
    image_quantization = []
    for i in range(image_compressed_row):
        for j in range(image_compressed_col):
            image_quantization.append(round(255 * (image_compressed[i][j] - min_value) / (max_value - min_value)))
    image_quantization = np.array(image_quantization).reshape(image_compressed_row, image_compressed_col)
    XS = []
    for i in range(image_compressed_row):
        for j in range(image_compressed_col):
            XS.append(255 * (image_compressed[i][j] - min_value) / (max_value - min_value) - image_quantization[i][j])
    XS = np.array(XS).reshape(image_compressed_row, image_compressed_col)
    return image_quantization, XS, max_value, min_value

def sensing_func(image_de_encryption, XS, max_value, min_value, x0, y0, p1, p2, CR, prow, a, b, arnold_iterations):
    row, col = np.array(image_de_encryption).shape
    image_deQuantization = []
    for i in range(row):
        for j in range(col):
            image_deQuantization.append(((image_de_encryption[i][j] - XS[i][j]) * (max_value - min_value) / 255) + min_value)
    image_deQuantization = np.array(image_deQuantization).reshape(row, col)
    hadamard_phi = hadamard_matrix(x0, y0, p1, p2, CR, prow)
    s1 = SL0(hadamard_phi, image_deQuantization, 1e-12, sigma_decrease_factor=0.2, L=3)
    s2 = arnold_decode(s1, a, b, arnold_iterations)
    image_deCompressed = cv2.idct(np.array(s2))
    return image_deCompressed



