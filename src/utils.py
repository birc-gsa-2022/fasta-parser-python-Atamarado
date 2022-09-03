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

# Compares a character or a space against the three different spaces contemplated (' ','\t','\n')
def isSpaceType(c):
    return c == ' ' or c == '\t' or c == '\n'
