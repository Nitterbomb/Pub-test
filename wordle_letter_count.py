file = open(r"C:\Users\enycz\Desktop\wordle_words.txt","r")
contents = [word.rstrip().upper() for word in contents]
file.close()
letter_counts = {chr(i+64): 0 for i in range(1,27)}
for word in contents:
    for letter in word:
        if letter in letter_counts:
            letter_counts[letter] += 1

for letter in sorted(letter_counts, key=letter_counts.get, reverse=True):
    print(letter, letter_counts[letter])
