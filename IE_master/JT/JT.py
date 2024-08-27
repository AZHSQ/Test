import numpy as np




def joseph_sequence(input_sequence, start, space):

    value = len(input_sequence)
    mark = np.zeros(value)
    scrambling = np.zeros(value)
    count1 = 0
    count2 = 0
    flag = 1

    while flag == 1:
        start = start % value
        if start == 0:
            start = value
        while count2 != space:
            while mark[start - 1] == 1:
                start += 1
                start = start % value
                if start == 0:
                    start = value
            count2 += 1
            start += 1
            start = start % value
            if start == 0:
                start = value
        start = (start - 1 + value) % value
        count2 = 0
        count1 += 1
        mark[start - 1] = 1
        scrambling[count1 - 1] = input_sequence[start - 1]
        if count1 == value:
            flag = 0

    return scrambling


def reverse_joseph_sequence(scrambled_sequence, start, space):
    value = len(scrambled_sequence)
    mark = np.zeros(value)
    original_sequence = np.zeros(value)
    count1 = 0
    count2 = 0
    flag = 1

    for i in range(1, value + 1):
        original_sequence[i - 1] = i

    while flag == 1:
        start = start % value
        if start == 0:
            start = value

        while count2 != space:
            while mark[start - 1] == 1:
                start += 1
                start = start % value
                if start == 0:
                    start = value
            count2 += 1
            start += 1
            start = start % value
            if start == 0:
                start = value

        start = (start - 1 + value) % value
        count2 = 0
        count1 += 1
        mark[start - 1] = 1
        original_sequence[start - 1] = scrambled_sequence[count1 - 1]

        if count1 == value:
            flag = 0

    return original_sequence



def to_decimal(binary_list):
    bin_list = []
    for i in range(len(binary_list)):
        bin_list.append(int(binary_list.tolist()[i]))
    binary_string = ''.join(map(str, bin_list))
    decimal_number = int(binary_string, 2)
    print(decimal_number)

