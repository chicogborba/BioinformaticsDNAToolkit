
import collections
from structures import *


# Chek sequence to make sure it is a DNA String
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(seq):
    return dict(collections.Counter(seq))


def transcription(seq):
    # DNA -> RNA Transcription
    return seq.replace("T", "U")


def reverseComplement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


def gcContent(seq):
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)


def gcContentSubsec(seq, k=20):
    res = []
    for i in range(0, len(seq) - k + 1, k):
        subseq = seq[i:i + k]
        res.append(gcContent(subseq))
    return res


def translateSeq(seq, init_pos=0):
    return [DNA_Codons[seq[pos:pos + 3]] for pos in range(init_pos, len(seq) - 2, 3)]


def codonUsage(seq, aminoacid):
    """Provides the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq) - 2, 3):
        if DNA_Codons[seq[i:i + 3]] == aminoacid:
            tmpList.append(seq[i:i + 3])

    freqDict = dict(collections.Counter(tmpList))
    totalWight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq] / totalWight, 2)
    return freqDict
