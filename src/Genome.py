class Genome:
    def __init__(self, name, chain):
        self.name = name
        self.chain = chain
    
    def __str__(self):
        return self.name+"\t"+self.chain
    
    def getName(self):
        return self.name
    
    def getChain(self):
        return self.chain
