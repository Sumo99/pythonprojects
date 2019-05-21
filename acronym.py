import re
import sys
import random

wordlist_filename = "/usr/share/dict/words"  # default word list location
if(len(sys.argv) != 2):
    sys.exit("This command is used like acronym.py 'word' no other arguments are nessecary")

word = list(sys.argv[1])  # split the word to make the acronym
file = open(wordlist_filename, "r")

def grepLetter(letter):  # search for a word starting with a letter of at least length four
    file.seek(0)  # reset the seek index so that we can read the file again
    matches = []
    search_string = f"^{letter}..."
    for line in file:
        if re.search(search_string, line):
            matches.append(line.strip())
    return matches


print()
print(f"The acyronym (or acrostic poem) for the word {sys.argv[1]} is as follows: ")
print()
for letters in word:
    results = grepLetter(letters)
    print(results[random.randrange(0, len(results))])
print()
#TODO make this more cross platform by exporting the file.
