import argparse
from Genome import Genome
from utils import *

# Returns the string and the index between the index pos until the character has been found
def findingSequence(chain, c, index):
    final = chain[index:].find(c)
    if final<0:
        return chain[index:], len(chain)
    else:
        return chain[index:index+final], index+final

# This method provides a way to get the proccessed content of a genome
def getGenomes(c):
    genomes = []

    length = len(c)

    # Find the symbol that tells us the beginning of a chromosome
    i = c.find(">")
    if i<0:
        return genomes

    while(i<length):
        i += 1
        # This first line is the name, which we are going to process
        name, i = findingSequence(c, "\n", i)
        name = name.strip()
        i += 1

        # Look for the genome
        genomeChain = ""
        if i<length:
            genomeChain, i = findingSequence(c, ">", i)

        genomeChain = stringG(genomeChain)
        gen = Genome(name, genomeChain)
        genomes.append(gen)
    
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
