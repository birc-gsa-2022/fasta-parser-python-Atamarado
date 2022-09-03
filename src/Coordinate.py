class Coordinate:
    def __init__(self, name, begin, end):
        self.name = name
        self.begin = begin
        self.end = end
    
    def __str__(self):
        return self.name+"\t"+str(self.begin)+"\t"+str(self.end)
