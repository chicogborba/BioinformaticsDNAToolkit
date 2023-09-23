from click import clear
from DNAToolkit import *
from utilities import colored
import random

# Test functions
rndDNASStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])

DNAStr = validateSeq(rndDNASStr)

clear()
print(f'\nSequence: {colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')
print(colored(f'[4] + DNA String + Reverse Complement:\n5\' {DNAStr} 3\''))
print(f"   {''.join(['|' for c in range(len(DNAStr))]) }")
print(colored(f'3\' {reverseComplement(DNAStr)[::-1]} 5\'\n'))
print(f'[5] + GC Content: {gcContent(DNAStr)}%\n')
print(f'[6] + GC Content in Subsection k=5: {gcContentSubsec(DNAStr, k=5)}\n')
print(f'[7] + Aminoacids Sequence from DNA: {translateSeq(DNAStr, 0)}\n')
print(f'[8] + Codon Frequency (L): {codonUsage(DNAStr, "L")}\n')
