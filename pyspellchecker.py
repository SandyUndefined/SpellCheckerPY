from spellchecker import SpellChecker

spell = SpellChecker()
char = input("Enter any string to check ")

print(spell.correction(str.lower(char)))  # correct the str
word = char.split()

# this can be further improved.
for i in word:
    print(spell.candidates(i))