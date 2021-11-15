import Myclass

m = Myclass.MorphologicalAnalyzer()
pt = Myclass.ParsedText()
parsed1 = m.parse("模範となる要約を作成し、その文章との類似度を計算する")
parsed1.setSum(5)
parsed2 = m.parse("すもももももももものうち")
parsed2.setSum(10)

pt.setSentence(parsed1)
pt.setSentence(parsed2)

print(pt.Get_by_Rank())