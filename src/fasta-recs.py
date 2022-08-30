import argparse
from email import contentmanager
import re


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
    
    index = 0

    while(index<len(content)):
        # Look for '> *'
        res = re.search(">(\s)*", content[index:]).end()
        if res<0:
            break
        index += res
        beginName = index

        # Look for the end of the name
        res = re.search("\s", content[index:]).start()
        if res<0:
            break
        index += res
        beginChain = index

        name = content[beginName:index]
        print(name, end=" ")
        
        # Look for the genome chain
        res = re.search(">", content[index:]).start()
        if res<0:
            break
        index += res
        
        # Delete spaces and intros
        chain = content[beginChain:index]
        chain = chain.replace("\s", "")
        chain = chain.replace("\n", "")
        print(chain)


if __name__ == '__main__':
    main()
