#!/use/bin/env python3
import sys
from MorphologicalAnalyzer import MorphologicalAnalyzer

ma = MorphologicalAnalyzer()

result_dict = {}
sentence_list = ['これはテストの文章です', 'これもテストです']
for sentence in sentence_list:
    parsed_sentence = ma.parse(sentence)
    word_list = map(lambda x: x.getWord(), parsed_sentence.getSentence())
    word_set = set(word_list)
    for word in word_set:
        if word not in result_dict:
            result_dict[word] = 0
        result_dict[word] += 1

with open(sys.argv[1], 'w') as f:
    for k, v in result_dict.items():
        f.write('{},{}\n'.format(k, v))
