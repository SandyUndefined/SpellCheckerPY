from spellchecker import SpellChecker


spell = SpellChecker()
str = input("Enter any string to check ")
print(spell.correction(str))  # correct the str
print(spell.candidates(str))  # provide lists of corrected word called candidates
