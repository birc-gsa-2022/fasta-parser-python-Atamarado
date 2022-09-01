import argparse
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
        match = re.search("\n", content[index:])
        if match is None:
            chain = content[beginName:len(content)]
            chain = re.sub('(\s)+',' ',chain).strip()
            print(chain, end="\t")
            break
        index += match.start()

        chain = content[beginName:index]
        chain = re.sub('(\s)+',' ',chain).strip()
        print(chain, end="\t")

        beginChain = index        
        # Look for the genome chain
        match = re.search(">", content[index:])
        #print(beginChain)
        if match is None:
            chain = content[beginChain:len(content)]
            chain = re.sub('\n','', chain) # Delete intros
            chain = re.sub('(\s)+',' ',chain).strip() # Replace spaces
            print(chain)
            break
        index += match.start()
        
        # Delete spaces and newlines
        chain = content[beginChain:index]
        chain = re.sub('\n','', chain) # Delete newlines
        chain = re.sub('(\s)+',' ',chain).strip() # Replace spaces
        print(chain)


if __name__ == '__main__':
    main()
