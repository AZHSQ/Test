


ADD = {}
ADD['AA'] = ADD['TG'] = ADD['CC'] = ADD['GT'] = 'A'
ADD['AT'] = ADD['TA'] = ADD['CG'] = ADD['GC'] = 'T'
ADD['AC'] = ADD['TT'] = ADD['CA'] = ADD['GG'] = 'C'
ADD['AG'] = ADD['TC'] = ADD['CT'] = ADD['GA'] = 'G'

SUB = {}
SUB['AA'] = SUB['TT'] = SUB['CC'] = SUB['GG'] = 'A'
SUB['AG'] = SUB['TA'] = SUB['CT'] = SUB['GT'] = 'T'
SUB['AC'] = SUB['TG'] = SUB['CA'] = SUB['GC'] = 'C'
SUB['AT'] = SUB['TC'] = SUB['CG'] = SUB['GA'] = 'G'

XOR = {}
XOR['AA'] = XOR['TT'] = XOR['CC'] = XOR['GG'] = 'A'
XOR['AT'] = XOR['TA'] = XOR['CG'] = XOR['GC'] = 'T'
XOR['AC'] = XOR['TG'] = XOR['CA'] = XOR['GT'] = 'C'
XOR['AG'] = XOR['TC'] = XOR['CT'] = XOR['GA'] = 'G'

UNADD = {}
UNADD['AA'] = UNADD['TT'] = UNADD['CC'] = UNADD['GG'] = 'A'
UNADD['AT'] = UNADD['TC'] = UNADD['CG'] = UNADD['GA'] = 'T'
UNADD['AC'] = UNADD['TG'] = UNADD['CA'] = UNADD['GT'] = 'C'
UNADD['AG'] = UNADD['TA'] = UNADD['CT'] = UNADD['GC'] = 'G'


def dna_unAdd(dna1, dnaRes):
    dna2 = ''
    for i in range(len(dna1)):
        dna2 += UNADD[dna1[i] + dnaRes[i]]

    return dna2


def dna_add(dna1, dna2):
    res = ''
    for i in range(len(dna1)):
        res += ADD[dna1[i] + dna2[i]]
    return res


def dna_sub(dna1, dna2):
    res = ''
    for i in range(len(dna1)):
        res += SUB[dna1[i] + dna2[i]]
    return res


def dna_xor(dna1, dna2):
    res = ''
    for i in range(len(dna1)):
        res += XOR[dna1[i] + dna2[i]]
    return res


