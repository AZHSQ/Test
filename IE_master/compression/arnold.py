import cv2
import numpy as np


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


def arnold_decode(matrix, a, b, iterations):
    width = len(matrix)
    height = len(matrix[0])
    N = len(matrix[0])
    for _ in range(iterations):
        new_matrix = [[0] * N for _ in range(N)]
        for x in range(width):
            for y in range(height):
                new_x = ((a * b + 1) * x - b * y) % N
                new_y = (-(a * x) + y) % N
                new_matrix[new_x][new_y] = matrix[x][y]
        matrix = new_matrix
    return matrix

