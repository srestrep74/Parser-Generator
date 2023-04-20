import nltk

class Process:
    def __init__(self,phrase,g):
        self.grammar = g
        self.phrase = phrase
    
    def validate(self):
        analizer = nltk.ChartParser(nltk.CFG.fromstring(self.grammar))
        validator = False
        try:
            for tree in analizer.parse(self.phrase.split()):
                if tree is not None: validator = True
            if validator: print("Yes")
            else: print("No")
        except ValueError as e :
            print(e)
