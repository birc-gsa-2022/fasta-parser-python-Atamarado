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
        match = re.search(">(\s)*", content[index:])
        if match is None:
            break
        index += match.end()
        beginName = index

        # Look for the end of the name
        match = re.search("\s", content[index:])
        if match is None:
            print(content[beginName:len(content)])
            break
        index += match.start()
        beginChain = index

        name = content[beginName:index]
        print(name, end="\t")
        
        # Look for the genome chain
        match = re.search(">", content[index:])
        if match is None:
            chain = content[index:len(content)]
            chain = re.sub('\n','', chain) # Delete intros
            chain = re.sub('\s+',' ',chain).strip() # Replace spaces
            print(chain)
            break
        index += match.start()
        
        # Delete spaces and intros
        chain = content[beginChain:index]
        chain = re.sub('\n','', chain) # Delete intros
        chain = re.sub('\s+',' ',chain).strip() # Replace spaces
        print(chain)


if __name__ == '__main__':
    main()
