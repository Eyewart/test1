"""attributs: value of scores
methods: -display_scores
-sum of scores via domino"""

class CDomino:
    def __init__(self,upvalue,downvalue):
        self.upvalue=upvalue
        self.downvalue=downvalue

    def DisplayDomino(self):
        domino=[self.upvalue,self.downvalue]
        print(domino)

    def SumDomino(self):
        sum=self.upvalue+self.downvalue
        return sum

