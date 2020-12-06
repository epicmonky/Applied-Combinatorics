import argparse

parser = argparse.ArgumentParser()
parser.add_argument("stringLength", type=int,
                    help="length of each word")

args = parser.parse_args()

alphabet = ['0', '1', '2', '3']

stringLength = args.stringLength

def makeAllWords(length):
    wordList = []
    
    if(length == 1):
        wordList = alphabet

    else:
        for char in alphabet:
            new_word = ""
            new_word += char
            for word in makeAllWords(length - 1):
                wordList.append(new_word + word)

    return wordList


def removeBadStrings(stringList):
    filteredList = [word for word in stringList if (word.find('11') == -1 and word.find('002') == -1)]
    return filteredList



if __name__ == '__main__':
    wordList = makeAllWords(stringLength)
    print(len(wordList))
    print(wordList)
    filteredList = removeBadStrings(wordList)
    print(filteredList)
    print(len(filteredList))

    """print(removeBadStrings(makeAllWords(2)))
    print(removeBadStrings(makeAllWords(3)))
    print(len(removeBadStrings(makeAllWords(3))))"""
    
