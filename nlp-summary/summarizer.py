import sys
import time

from weighter import Weighter
from MorphologicalAnalyzer import MorphologicalAnalyzer
from calced_word import CalcedWord
from parsed_sentence import ParsedSentence
from parsed_text import ParsedText

class Summarizer:
    def __init__(self):
        self.weighter = None
        self.file_name = None
        self.summary = ""
        self.max_length = 0

        self.parsed_text = ParsedText()
        self.parser = MorphologicalAnalyzer()
        
        self.file = None

    def summalize(self, file_name, max_length):
        self.file_name = file_name
        self.max_length = max_length
        self.weighter = Weighter(153)#ぐらい
        self.weighter.load_idf("idf.txt")

        try:
            file = open(self.file_name, "rt")
        except OSError as e:
            print(e)

        for line in iter(file.readline, ''):
            print("for line in iter(file.readline, ''): " + line)
            self.parsed_text.setSentence(self.parser.parse(line))
            
        self.weighter.calc_tf(self.parsed_text)

        pt = ParsedText()
        for sentence in self.parsed_text:
            print("sentence.weight_sum()")

            pt.setSentence(self.weighter.weight_sentence(sentence))
            sentence.calcSum()

        self.parsed_text = pt
        for sentence in self.parsed_text:
            print("sentence.weight_sum()")
            sentence.calcSum()

        count = 1
        while len(self.summary) < self.max_length:
            # print(self.summary)
            ret = str(self.parsed_text.get_by_Rank(count))
            if len(self.summary) + len(ret) >= self.max_length:
                break    
            self.summary += ret
            count += 1

        return self.summary

#test
if __name__ == "__main__":
    summarizer = Summarizer()
    ret = summarizer.summalize(sys.argv[1], 140)
    print("----要約----")
    print(ret)
    print("----要約ここまで----")