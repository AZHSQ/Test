from _operator import xor
from operator import mod, or_


from diffusion.CRT import compute_remainders


def complementary(dna, rule, L):
    dna_complementary_mapping = {
        0: {"A": "T", "T": "C", "C": "G", "G": "A"},
        1: {"A": "t", "T": "G", "G": "C", "C": "A"},
        2: {"A": "C", "C": "G", "G": "T", "T": "A"},
        3: {"A": "C", "C": "T", "T": "G", "G": "A"},
        4: {"A": "G", "G": "C", "C": "T", "T": "A"},
        5: {"A": "G", "G": "T", "T": "C", "C": "A"},
    }
    #
    for _ in range(L):
        dna = dna_complementary_mapping[rule].get(dna, dna)
    return dna

def complementary_list(dna_str, rule, L, c1, c2, c3, c4):
    dna_complementary_mapping = {
        0: {"A": "T", "T": "C", "C": "G", "G": "A"},
        1: {"A": "T", "T": "G", "G": "C", "C": "A"},
        2: {"A": "C", "C": "G", "G": "T", "T": "A"},
        3: {"A": "C", "C": "T", "T": "G", "G": "A"},
        4: {"A": "G", "G": "C", "C": "T", "T": "A"},
        5: {"A": "G", "G": "T", "T": "C", "C": "A"},
    }

    moduli = [c1, c2, c3, c4]
    rule_list = compute_remainders(rule, moduli)
    rule_list = [mod(element, 6) for element in rule_list]
    L_list = compute_remainders(L, moduli)
    L_list = [mod(element, 4) for element in L_list]
    complementary_str = ""
    for i, nucleotide in enumerate(dna_str):
        rule = rule_list[i % 4]
        L = L_list[i % 4]
        for _ in range(L):
            nucleotide = dna_complementary_mapping[rule].get(nucleotide, nucleotide)
        complementary_str += nucleotide
    return complementary_str

def reverse_complementary(complementary_str, rule, L, c1, c2, c3, c4):
    dna_complementary_mapping = {
        0: {"A": "T", "T": "C", "C": "G", "G": "A"},
        1: {"A": "T", "T": "G", "G": "C", "C": "A"},
        2: {"A": "C", "C": "G", "G": "T", "T": "A"},
        3: {"A": "C", "C": "T", "T": "G", "G": "A"},
        4: {"A": "G", "G": "C", "C": "T", "T": "A"},
        5: {"A": "G", "G": "T", "T": "C", "C": "A"},
    }
    moduli = [c1, c2, c3, c4]
    rule_list = compute_remainders(rule, moduli)
    rule_list = [mod(element, 6) for element in rule_list]
    L_list = compute_remainders(L, moduli)
    L_list = [4 - mod(element, 4) for element in L_list]

    dna_str = ""
    for i, nucleotide in enumerate(complementary_str):
        rule = rule_list[i % 4]
        L = L_list[i % 4]
        for _ in range(L):
            nucleotide = dna_complementary_mapping[rule].get(nucleotide, nucleotide)
        dna_str += nucleotide
    return dna_str



