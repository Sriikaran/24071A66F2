from collections import Counter

def most_common_word(text):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(1)[0]

text = "word word hi word word"
print(most_common_word(text)) 
