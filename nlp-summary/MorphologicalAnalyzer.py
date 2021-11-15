import MeCab

# 形態素解析に関するクラス		
class MorphologicalAnalyzer():
	def parse(self, str): # MeCabの解析結果を返すメソッド/引数は文字列
		mecab = MeCab.Tagger("-Owakati")
		parsed = mecab.parse(str).split(' ')

		return parsed

# MeCabによって分解された単語とその重みを表すクラス		
class CalcedWord():
	def getWord(self): # 単語ゲッター
		return self.word
	def getWeight(self): # 重みゲッター
		return self.weight

# CalcedWordを集めた文とその重み合計を表すクラス
class ParsedSentence():
	def getSentence(self): # 文ゲッター
		return list
	def getSum(self): # 重みゲッター
		return sum

# ParsedSentenceを集めた文章を表すクラス
class ParsedText():
	def getText(self): # 文章ゲッター
		return list