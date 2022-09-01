import argparse

# Gets the name of the chromosome in the required format
def stringN(string):
    return string.strip()+'\t'

# Gets the chromosome in the required format
def stringG(string):
    return deleteSpacing(string)+'\n'

# Deletes all space-like characters from a string
def deleteSpacing(string):
    output = ""
    for c in string:
        if c != " " and c != "\t" and c != "\n":
            output += c
    return output

# This method provides a way to get the proccessed content of a genome
def stringGenome(c):
    output = ""

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
                return output
        
        # Store all the name
        while c[i] != '\n':
            chain += c[i]
            i += 1
            if i >= length:
                return output+stringN(chain)
        
        output += stringN(chain)
        chain = ""

        i += 1
        if i>=length:
            return

        # Look for the genome
        while c[i] != '>':
            chain += c[i]
            i += 1
            if i >= length:
                return output+stringG(chain)

        output += stringG(chain)
        chain = ""
    
    return output


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

    output = stringGenome(content)
    print(output, end='')

if __name__ == '__main__':
    main()
