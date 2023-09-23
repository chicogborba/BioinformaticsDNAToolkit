
def readFile(filePath):
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]


def gcContent(seq):
    return ((seq.count('C') + seq.count('G')) / len(seq) * 100)


FASTAFile = readFile('stronghold/test_data/gc_content.txt')
FASTADict = {}
FASTALabel = ''

for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ''
    else:
        FASTADict[FASTALabel] += line

RESULTDict = {key: gcContent(value) for key, value in FASTADict.items()}

RESULTLabel = max(RESULTDict, key=RESULTDict.get)
RESULTValue = RESULTDict[RESULTLabel]

print(RESULTLabel[1:])
print(RESULTValue)
