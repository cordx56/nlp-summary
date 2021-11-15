import MeCab
import pandas
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
	wsum = 0
	def setWord(self, word):
		self.sent.append(word)
	def setSum(self, n):
		self.wsum = n
	def calcSum(self):
		for i in range(0,len(sent)):
			self.wsum += sent[i].getWeight()
		return wsum
	def getSentence(self): # 文ゲッター
		return self.sent
	def getSum(self): # 重みゲッター
		return self.wsum

# ParsedSentenceを集めた文章を表すクラス
class ParsedText():
	txt = []
	def setSentence(self, sent):
		self.txt.append(sent)
	def getText(self): # 文章ゲッター
		return self.txt
	def Get_by_Rank(self): # 引数で与えられた順位のsentを出力
		df = pandas.DataFrame(self.txt)
		sortedDF = df.sort_values('1')
		rtxt = sortedDF.values.tolist()

		return self.rtxt