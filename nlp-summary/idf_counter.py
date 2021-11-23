#!/use/bin/env python3
import sys
import os
from pathlib import Path

from MorphologicalAnalyzer import MorphologicalAnalyzer

ma = MorphologicalAnalyzer()

def count_idf(dir_name):
    p = Path(dir_name)
    if(not p.exists()):
        return

    result_dict = {}
    sentence_list = make_sentence_list(p)
    for i, sentence in enumerate(sentence_list):
        print(i)
        parsed_sentence = ma.parse(sentence)
        word_list = map(lambda x: x.getWord(), parsed_sentence.getSentence())
        word_set = set(word_list)
        for word in word_set:
            if ',' in word:
                continue
            if word not in result_dict:
                result_dict[word] = 0
            result_dict[word] += 1

    with open(sys.argv[1] + "/idf.txt", 'w') as f:
        for k, v in result_dict.items():
            f.write('{},{}\n'.format(k, v))

def make_sentence_list(p):
    l = list()
    for target in p.glob("*.txt"):
        print(target)
        with open(target) as f:
            l.append(f.read())
    print(l)
    return l

if __name__ == "__main__":
    count_idf(sys.argv[1] + "/")
