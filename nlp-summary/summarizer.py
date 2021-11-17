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
        self.weighter = Weighter(160)#ぐらい

        try:
            file = open(self.file_name, "rt")
        except OSError as e:
            print(e)

        for line in iter(file.readline, ''):
            print(line)
            self.parsed_text.setSentence(self.parser.parse(line))
            
        self.weighter.calc_tf(self.parsed_text)

        for sentence in self.parsed_text:
            sentence.weight_sum()

        count = 1
        while len(self.summary) < self.max_length:
            # print(self.summary)
            ret = str(self.parsed_text.get_by_Rank(count))
            if len(self.summary) + len(ret) >= self.max_length:
                break    
            self.summary += ret
            count += 1

        return self.summary

#dummy
# class Weighter:
#     def __init__(self):
#         print("Weighter.__init__()")
#         pass
#     def calc_tf(self, parsed_text):
#         pass

# class MorphologicalAnalyzer:
#     def __init__(self):
#         print("MorphologicalAnalyzer.__init__()")
#         pass
#     def parse(self, str):
#         print("MorphologicalAnalyzer.parse()")
#         pass

# class ParsedText:
#     def __init__(self):
#         print("ParsedText.__init__()")
#         self.i = 0
#         self.parsed_sentences = [ParsedSentence()]
#         pass

#     def add(self, parsed_sentence):
#         print("ParsedText.add()")
#         pass

#     def __iter__(self):
#         self.i = 0
#         return self
    
#     def __next__(self):
#         print("ParsedText.__next__()")
#         if self.i > 5 : raise StopIteration
#         self.i += 1
#         return self.parsed_sentences[0]
    
#     def get_by_Rank(self, rank):
#         #weight の高い順にrank番目のものが帰ってくると良い
#         print("ParsedText.get_by_Rank()")
#         return("ランクの高い1文")

# class ParsedSentence:
#     def __init__(self):
#         print("ParsedSentence.__init__()")
#         self.list = None
#     def weight_sum(self):
#         pass
#     def __str__(self):
#         return "listから文字列化したやつ"

# class CalcedWord:
#     def __init__(self):
#         print("CalcedWord.__init__()")
#         self.word = ""
#         self.weight = 0.0

#test
if __name__ == "__main__":
    summarizer = Summarizer()
    ret = summarizer.summalize("../testText.txt", 140)
    print("----要約----")
    print(ret)
    print("----要約ここまで----")