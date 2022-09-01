import argparse
from bdb import Breakpoint
import sys
from fastaRecs import getGenomes
from Genome import Genome
from Coordinate import Coordinate
from utils import *

# Process the cords and adds them to a list of Coordinates
def processCords(c):
    coordinates = []

    i = 0
    length = len(c)

    while i<length:
        line = ""
        while i<length and c[i] != '\n': # Process an entire line
            line += c[i]
            i+=1
        i += 1

        words = line.split()
        if len(words) < 3:
            print("Insufficient arguments for the line. Format: name begin end")
        else: # Process all words until n-2
            j = 0
            wordsProcessed = 0
            name = ""
            # Get the name
            while(wordsProcessed<len(words)-2):
                while line[j] == ' ' or line[j] == '\t':
                    name += line[j]
                    j += 1
                while not(line[j] == ' ' or line[j] == '\t'):
                    name += line[j]
                    j+= 1
                wordsProcessed += 1
            name = stringN(name)
            # Get begin and end of the number. We substract one to start counting in 0
            begin = int(words[len(words)-2]) - 1
            end = int(words[len(words)-1]) - 1

            coordinate = Coordinate(name, begin, end)
            coordinates.append(coordinate)         

    return coordinates

# Returns a string containing the subsequence of a chromosome indicated by coord (both the name and positions)
def getSubsequence(genomes, coord):
    # First of all, we have to find the genome to extract the subsequence
    coordName = coord.getName()
    begin = coord.getBegin()
    end = coord.getEnd()
    for gen in genomes:
        if coordName == gen.getName():
            return gen.getChain()[begin:end]

def main():
    argparser = argparse.ArgumentParser(
        description="Extract sub-sequences from a Simple-FASTA file"
    )
    argparser.add_argument(
        "fasta",
        type=argparse.FileType('r')
    )
    argparser.add_argument(
        "coords",
        nargs="?",
        type=argparse.FileType('r'),
        default=sys.stdin
    )
    args = argparser.parse_args()

    # print(f"Now I need to process the records in {args.fasta}")
    # Read the content
    content = args.fasta.read()
    genomes = getGenomes(content)

    # print(f"and the coordinates in {args.coords}")
    content = args.coords.read()
    coordinates = processCords(content)

    for coord in coordinates:
        print(getSubsequence(genomes, coord))


if __name__ == '__main__':
    main()
