from textblob import TextBlob, Word
sentence = TextBlob("he wass verry siccck ")
print(sentence.correct())
word = Word("gooa")
print(word.spellcheck())
