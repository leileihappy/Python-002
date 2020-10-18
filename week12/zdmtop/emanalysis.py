from snownlp import SnowNLP

class EmAnalysis:
    def analysis(self,text):
        s = SnowNLP(text)
        return s.sentiments