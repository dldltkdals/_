N = int(input())
from collections import defaultdict
words = [input() for i in range(N)]

prefix = defaultdict(list)

for inx,word in enumerate(words):
    for i in range(len(word)):
        prefix[word[:i+1]].append(inx)
max_len = float("-inf")
max_inx = []
for word, inx in prefix.items():
    word_len = len(word)
    if len(inx) >= 2:
        if word_len > max_len:
            max_len = word_len
            max_inx = inx
        elif word_len == max_len:
            if max_inx[0] > inx[0]:
                max_inx = inx
for i in range(2):
    print(words[max_inx[i]])