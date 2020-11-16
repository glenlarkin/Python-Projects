#!python3
# Lower cases all words in string, except the first word in the sentence

context = input('Enter any words you would like to De-Capitalize:\n')

allLow = context.lower()

sentenceStart = allLow[0].capitalize()
sentenceEnd = allLow[1:]
result = sentenceStart + sentenceEnd
print(result)