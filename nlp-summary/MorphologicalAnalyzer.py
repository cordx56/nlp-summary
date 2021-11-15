import MeCab

# 形態素解析に関するクラス		
class MorphologicalAnalyzer():
	def parse(self, str): # MeCabの解析結果を返すメソッド/引数は文字列
		ps = ParsedSentence()
		mecab = MeCab.Tagger("-Owakati")
		parsed = mecab.parse(str).split(' ')

		for i in range(0,len(parsed)):
			cw = CalcedWord(parsed[i])
			ps.setWord(cw)

		return ps.getSentence()

# MeCabによって分解された単語とその重みを表すクラス		
class CalcedWord():
	def __init__(self, w):
		self.weight = 0
		self.word = w
	def getWord(self): # 単語ゲッター
		return self.word
	def getWeight(self): # 重みゲッター
		return self.weight

# CalcedWordを集めた文とその重み合計を表すクラス
class ParsedSentence():
	sent = []
	def setWord(self, word):
		self.sent.append(word)
	def getSentence(self): # 文ゲッター
		return self.sent
	def getSum(self): # 重みゲッター
		return sum

# ParsedSentenceを集めた文章を表すクラス
class ParsedText():
	def getText(self): # 文章ゲッター
		return list
