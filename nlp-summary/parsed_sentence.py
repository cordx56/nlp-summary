from typing import Optional, List
from calced_word import CalcedWord

class ParsedSentence():
	def __init__(self):
		self.sent = [] #文(CalcedWordのlist)
		self.wsum = 0 #重み合計
	def setWord(self, word): #listにCalcedWordをセットするメソッド
		self.sent.append(word)
	def setSum(self, n): #デバッグ用、重み合計をセットするメソッド
		self.wsum = n
	def calcSum(self): #重み合計を計算するメソッド	
		self.wsum = 0
		for i in range(0,len(self.sent)):
			self.wsum += self.sent[i].getWeight()
		print(str(self) + ":" + str(self.wsum))
		return self.wsum
	def getSentence(self): #文ゲッター
		return self.sent
	def getSum(self): #重みゲッター
		return self.wsum

	def __str__(self):
		out_str = ""
		for i in range(0,len(self.sent)):
			out_str += self.sent[i].getWord()
		return out_str