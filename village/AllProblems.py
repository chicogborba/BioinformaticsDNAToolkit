# import this

# =========== Variables and Some Arithmetic ===========
a = 941
b = 860
print(f'{a}ˆ2 + {b}ˆ2 = {a**2 + b**2}')

# ============ Strings and Lists ============
wordOneStartPos = 8
wordOneEndPos = 10

wordTwoStartPos = 79
wordTwoEndPos = 87

txtStr = "yzqZJfjkBoaZxraRVl7m9nR6klEMyuBN0ZATkk6nAnYVa03LLZiTyvqdrD5hSoFDqr1deUmJtZKFipTmarcianus1at8esI6FYwroGQg9YdE4UW7DkV7g8AItXz0IH0jttKUpe2JAHHSBRhcHvDNUGBeJxy8mCpcll8jasdixrydsX3Yh"

# End position is not inclusive, so we add 1 to capture it
# print(
#     f'{txtStr[wordOneStartPos:wordOneEndPos+1]} {txtStr[wordTwoStartPos:wordTwoEndPos+1]}'
# )

# ============ Conditions and Loops ============

a = 4014
b = 8202

sum = 0

for i in range(a, b+1):
    if i % 2 != 0:
        sum += i

# print(sum)

# ============ Dictionaries ============

# Given: A string s
# of length at most 10000 letters.

# Return: The number of occurrences of each word in s
# , where words are separated by spaces. Words are case-sensitive, and the lines in the output can be in any order.

s = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

words = s.split(" ")

wordCount = {}

for word in words:
    if word in wordCount:
        wordCount[word] += 1
    else:
        wordCount[word] = 1

# for word in wordCount:
#     print(f'{word} {wordCount[word]}')

# ============ Working with Files ============

# Problem
# Given: A file containing at most 1000 lines.

# Return: A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.

# Sample Dataset
# Bravely bold Sir Robin rode forth from Camelot
# Yes, brave Sir Robin turned about
# He was not afraid to die, O brave Sir Robin
# And gallantly he chickened out
# He was not at all afraid to be killed in nasty ways
# Bravely talking to his feet
# Brave, brave, brave, brave Sir Robin
# He beat a very brave retreat

# Sample Output
# Yes, brave Sir Robin turned about
# And gallantly he chickened out
# Bravely talking to his feet
# He beat a very brave retreat


outputFile = []

with open('village/input.txt', 'r') as f:
    outputFile = [line for pos, line in enumerate(
        f.readlines()) if pos % 2 != 0]

with open('village/input.txt', 'w') as f:
    f.write(''.join([line for line in outputFile]))
