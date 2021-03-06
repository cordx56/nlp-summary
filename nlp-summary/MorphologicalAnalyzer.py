import MeCab
from calced_word import CalcedWord
from parsed_sentence import ParsedSentence
from parsed_text import ParsedText

# 形態素解析に関するクラス		
class MorphologicalAnalyzer():
    def parse(self, str): # MeCabの解析結果をParsedSentence型で返すメソッド/引数は文字列
        ps = ParsedSentence()
        mecab = MeCab.Tagger("-Owakati")
        parsed = mecab.parse(str).split(' ')
        parsed = filter(lambda x: len(x.strip()) != 0, parsed)
        parsed = filter(lambda x: "," not in x, parsed)

        for v in parsed:
            cw = CalcedWord(v)
            ps.setWord(cw)

        return ps

