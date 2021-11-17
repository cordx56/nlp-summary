from typing import List
from parsed_sentence import ParsedSentence

# ParsedSentenceを集めた文章を表すクラス
class ParsedText():
	def __init__(self):
		self.txt = [] #文章(ParsedSentenceのlist)
		self._i = 0
	
	def setSentence(self, sent): #listにParsedSentenceをセットするメソッド
		self.txt.append(sent)
	def getText(self): # 文章ゲッター
		return self.txt
	def get_by_Rank(self, rank): # 引数で与えられた順位のsentを出力
		rtxt = sorted(self.txt, key=lambda ParsedSentence: ParsedSentence.wsum)
		return rtxt[rank-1]
	def __iter__(self):
		# __next__()はselfが実装してるのでそのままselfを返す
		return self
	def __next__(self):  # Python2だと next(self) で定義
		if self._i == len(self.txt):
			raise StopIteration()
		value = self.txt[self._i]
		self._i += 1
		return value