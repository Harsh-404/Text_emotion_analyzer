import string

from collections import Counter
import matplotlib.pyplot as plt
text = open("read.txt", encoding="utf-8").read()
low_case = text.lower()
clear_text = low_case.translate(str.maketrans('', '', string.punctuation))
split_text = clear_text.split()

explicit_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
final_word = []
for word in split_text:
    if word not in explicit_words:
        final_word.append(word)

emotion_list = []
with open('emot.txt', 'r') as file:
    for line in file:
        clean_text =line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clean_text.split(':')

        if word in final_word:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.jpg')
plt.show()
