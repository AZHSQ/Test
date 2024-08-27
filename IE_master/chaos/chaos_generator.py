import math



def generate_chaos_sequence(x0, y0, a, b, m, n):
    x_sequence = []
    y_sequence = []
    iterations = m * n * 3
    for _ in range(iterations):
        x = math.pow(math.sin(a * math.pow(math.pi, 2) * (math.log(x0) / math.exp(y0) + math.log(y0) / math.exp(x0))),2)
        y = math.pow(math.sin(b * math.pow(math.pi, 2) * (math.log(x0 * y0) / math.exp(x0 * y0))), 2)
        x_sequence.append(x)
        y_sequence.append(y)

        x0 = x
        y0 = y
    return x_sequence[-(m * n):], y_sequence[-(m * n):], x_sequence[-2 * (m * n):-m * n], y_sequence[-2 * (m * n):-m * n]  #  截取x、y 最后m*n个元素 和  倒数第二个m*n个元素



