from operator import mod

import numpy as np


def encode_to_dna(binary_str, ruleNumber):


    dna_mapping = {
        0: {"00": "A", "11": "T", "10": "C", "01": "G"},
        1: {"00": "A", "11": "T", "01": "C", "10": "G"},
        2: {"11": "A", "00": "T", "10": "C", "01": "G"},
        3: {"11": "A", "00": "T", "01": "C", "10": "G"},
        4: {"10": "A", "01": "T", "00": "C", "11": "G"},
        5: {"01": "A", "10": "T", "00": "C", "11": "G"},
        6: {"10": "A", "01": "T", "11": "C", "00": "G"},
        7: {"01": "A", "10": "T", "11": "C", "00": "G"}
    }

    dna_sequence = ""
    for i in range(0, len(binary_str),2):
        bits = binary_str[i:i+2]
        if bits in dna_mapping.get(ruleNumber, {}):
            dna_sequence += dna_mapping[ruleNumber][bits]
    return dna_sequence

def decode_dna_to_binary(dna_sequence, ruleNumber):
    dna_reverse_mapping = {
        0: {"A": "00", "T": "11", "C": "10", "G": "01"},
        1: {"A": "00", "T": "11", "C": "01", "G": "10"},
        2: {"A": "11", "T": "00", "C": "10", "G": "01"},
        3: {"A": "11", "T": "00", "C": "01", "G": "10"},
        4: {"A": "10", "T": "01", "C": "00", "G": "11"},
        5: {"A": "01", "T": "10", "C": "00", "G": "11"},
        6: {"A": "10", "T": "01", "C": "11", "G": "00"},
        7: {"A": "01", "T": "10", "C": "11", "G": "00"}
    }

    binary_sequence = ""

    for base in dna_sequence:
        if base in dna_reverse_mapping.get(ruleNumber, {}):
            binary_sequence += dna_reverse_mapping[ruleNumber][base]

    return binary_sequence