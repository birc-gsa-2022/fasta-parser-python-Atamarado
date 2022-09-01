import argparse

# Prints the name of the chromosome in the required format
def printN(string):
    print(string.strip(), end='\t')

# Prints the chromosome in the required format
def printG(string):
    print(deleteSpacing(string))

# Deletes all space-like characters from a string
def deleteSpacing(string):
    output = ""
    for c in string:
        if c != " " and c != "\t" and c != "\n":
            output += c
    return output

# This method provides a way to print the proccessed content of a genome
def printGenome(c):
    length = len(c)
    i = 0

    # Find the symbol that tells us the beginning of a chromosome
    while  c[i] != '>':
        i += 1
        if i >= length:
            return
    
    chain = ""

    while(i<length):        
        i += 1

        # Find the beginning of the name
        while c[i] == ' ' or c[i] == '\t' or c[i] == '\n':
            i += 1
            if i >= length:
                return
        
        # Store all the name
        while c[i] != '\n':
            chain += c[i]
            i += 1
            if i >= length:
                printN(chain)
                return
        
        printN(chain)
        chain = ""

        i += 1
        if i>=length:
            return

        # Look for the genome
        while c[i] != '>':
            chain += c[i]
            i += 1
            if i >= length:
                printG(chain)
                return

        printG(chain)
        chain = ""


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

    printGenome(content)

if __name__ == '__main__':
    main()
