import re
anagrams = {}
paragraph = input("Give your paragraph: ")
punctuation_remove = lambda words: re.sub(r'[^a-zA-Z0-9\s]', "", words)
clean_string = punctuation_remove(paragraph)

for word in clean_string.split(" "):
    sorted_word = "".join(sorted(word.lower()))
    anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]

for k , v in anagrams.items():
    if len(v) > 1:
        print(f"{k}: {' '.join(v)}")


