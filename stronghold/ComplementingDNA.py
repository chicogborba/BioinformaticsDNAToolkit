
DNA_ReverseComplement = {"A": "T", "C": "G", "G": "C", "T": "A"}


DNA = "TCGACATACTTCGGCTTTGTACGCCTTCACAGCACAGTTCTTGATCCCCTTTTCCAAAGTGAACAAAAATTAATTCCCTTGCGTTGATCTTGTATTCAGTCACCCCCAGAATGAAGCTGCTCGGTGGTCGGGGTGTGGAATCCTTCTGGAAATTGCCGGAAGCATTTGACGTTTCGGGGTTGGCTCAGGCTTATAGTTTCGCTACCCGCCGGCCACACATCGAGATCTAGGATGCGGCTTCACCGGCCTGATAGGGATTTAAGATCTAGCATCGGACGTTAAGGGTCCAAAATGCGAGAGCTGTGCTTCAGTCTCTTATACTGGCAGACGCGATCAGTGTTTTGAGTGGTGCCCTAATTCCACGTCTGAACAGAGACGAACTACCCTTGGTCGGGATCATACGGAGTCTGCTATGGGCTTTAGAGGCTTTTCATACGGCGGTGAAACCGGAGTGGCGGTTGAACTCGAGTTCTCCTACGGCTCGTGCGAGCTATTACTGCTCGTCAAGTGCTATCAATCATAAGCAGAGGAAAAATAGTGGTCGTATAAGGAAGCGGCAAGTGCGTTCATCTATCCCATGCGCTAACACTATCCTTGTAGACATGCCTAATCATGACGATACGATATGCTTGAGGAATATGCGCCGCGTTCAACTACGAATGTAGCAAACTTGTCCATTGGGTTTGAACAATTCCGGAACATGTAACCGAGATTTTCAACGCTCAGGGGGGAACTTCTCCAAGTACTAACAACACCTGTCGTCCATGGGATTCATTGCACGACTTACCTTGCACCTTCGCCGGGTTGCTGTGTAGATGATCTACCGTTGATCACTGTATACGTAAAAAGACTGGCAAGAATACCGTATTCTGACTTCGATCTTAGTTTCCTTTTTGAGCCCTGCCCCTTATAAATTGAAACCTAAGGTGCCGCTGATATCGACATTGCCAGCTAAACCGAAAGATGCAGATGGTGTAATTCCCTACACGA"


def reverseComplement(seq):
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])[::-1]


print(reverseComplement(DNA))
