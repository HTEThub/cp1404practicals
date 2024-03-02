"""
Word Occurrences
Estimate: 30 minutes
Actual: 29 minutes 53 seconds
"""

text_to_count = {}
longest_word = 0

text_input = input("Text: ")
words = text_input.split()
words.sort()
# print(words)
for eachWord in words:
    if eachWord in text_to_count:
        text_to_count[eachWord] += 1
    else:
        text_to_count[eachWord] = 1

    if len(eachWord) > longest_word:
        longest_word = len(eachWord)


for eachKey in text_to_count:
    print(f"{eachKey:{longest_word}} : {text_to_count[eachKey]}")

