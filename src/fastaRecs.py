import argparse
from Genome import Genome
from utils import isSpaceType

# Gets the name of the chromosome in the required format
def stringN(string):
    return string.strip()

# Gets the chromosome in the required format
def stringG(string):
    return deleteSpacing(string)

# Deletes all space-like characters from a string
def deleteSpacing(string):
    output = ""
    for c in string:
        if not(isSpaceType(c)):
            output += c
    return output

# This method provides a way to get the proccessed content of a genome
def getGenomes(c):
    genomes = []

    length = len(c)
    i = 0

    # Find the symbol that tells us the beginning of a chromosome
    while  c[i] != '>':
        i += 1
        if i >= length:
            return
    
    name = None
    genomeChain = None
    chain = ""

    while(i<length):        
        i += 1

        # Find the beginning of the name
        while isSpaceType(c[i]):
            i += 1
            if i >= length:
                return genomes
        
        # Store all the name
        while c[i] != '\n':
            chain += c[i]
            i += 1
            if i >= length:
                break
        
        name = stringN(chain)
        chain = ""

        i += 1
        if i<length:
            # Look for the genome
            while c[i] != '>':
                chain += c[i]
                i += 1
                if i >= length:
                    break

        genomeChain = stringG(chain)
        gen = Genome(name, genomeChain)
        genomes.append(gen)

        chain = ""
    
    return genomes


def main():
    argparser = argparse.ArgumentParser(
        description="Extract Simple-FASTA records"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    args = argparser.parse_args()

    # Read the content
    content = args.fasta.read()

    genomes = getGenomes(content)
    for gen in genomes:
        print(gen)

if __name__ == '__main__':
    main()
