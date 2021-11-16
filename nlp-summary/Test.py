import MorphologicalAnalyzer

m = MorphologicalAnalyzer.MorphologicalAnalyzer()
pt = MorphologicalAnalyzer.ParsedText()
parsed1 = m.parse("模範となる要約を作成し、その文章との類似度を計算する")
parsed1.setSum(5)
parsed2 = m.parse("すもももももももものうち")
parsed2.setSum(10)

print(parsed1.getSum())
print(parsed2.getSum())

pt.setSentence(parsed1)
pt.setSentence(parsed2)

sent = pt.Get_by_Rank(1).getSentence()
for i in range(0,len(sent)):
	print(sent[i].getWord())