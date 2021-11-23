from typing import Dict
import math
from calced_word import CalcedWord
from parsed_sentence import ParsedSentence
from parsed_text import ParsedText

class Weighter:
    tf_dictionary: Dict[str, float] = {}
    idf_dictionary: Dict[str, int] = {}
    docments_count: int = 0
    def __init__(self, n: int):
        self.documents_count = n
    def weight(self, source: str) -> CalcedWord:
        result = CalcedWord(source)
        #result.word = source
        #print(self.tf_dictionary[result.word])
        #print(self.idf_dictionary[result.word])
        try:
            result.weight = self.tf_dictionary[result.word]
            result.weight *= math.log2(self.documents_count / self.idf_dictionary[result.word]) + 1
        except KeyError as e:
            result.weight = 0
        #print(str(result))
        return result
    def weight_sentence(self, source: ParsedSentence) -> ParsedSentence:
        result = ParsedSentence()
        for source_word in source.sent:
            result_word = self.weight(source_word.word)
            result.setWord(result_word)
        return result
    def calc_tf(self, source: ParsedText):
        word_count = 0
        for parsed_sentence in source:
            for calced_word in parsed_sentence.sent:
                word = calced_word.word
                if word not in self.tf_dictionary.keys():
                    self.tf_dictionary[word] = 0
                self.tf_dictionary[word] += 1
                word_count += 1
        for v in self.tf_dictionary:
            self.tf_dictionary[v] /= word_count
    
    def load_idf(self, filename: str):
        with open(filename, 'r') as f:
            for line in f.readlines():
                splitted = line.split(',')
                self.idf_dictionary[splitted[0]] = int(splitted[1])
