class Coordinate:
    def __init__(self, name, begin, end):
        self.name = name
        self.begin = begin
        self.end = end
    
    def __str__(self):
        return self.name+"\t"+str(self.begin)+"\t"+str(self.end)
    
    def getName(self):
        return self.name
    
    def getBegin(self):
        return self.begin
    
    def getEnd(self):
        return self.end
