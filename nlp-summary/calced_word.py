from typing import Optional

class CalcedWord():
	def __init__(self, w):
		self.weight = 0 #重み
		self.word = w #単語
	def getWord(self): # 単語ゲッター
		return self.word
	def getWeight(self): # 重みゲッター
		return self.weight