wordset = set()
with open('傲慢与偏见英文版.txt', 'r') as f:
    for line in f.readlines():
        words = line.split(" ")
        for word in words:
            wordset.add(word.strip(","))

with open("target_words.txt", "w") as f:
    for i in list(wordset)[:30]:
        f.write(i)
        f.write("\n")
    