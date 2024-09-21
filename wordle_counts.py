file = open(r"C:\Users\enycz\Desktop\wordle_words.txt","r")
contents = [word.rstrip().upper() for word in file.readlines()]
file.close()
letter_counts = {chr(i+64): 0 for i in range(1,27)}
letter_positions = {chr(i+64): {j: 0 for j in range(1,6)} for i in range(1,27)}
for word in contents:
    k = 1
    for letter in word:
        if letter in letter_positions:
            letter_counts[letter] += 1
            letter_positions[letter][k] += 1
        k += 1
print (f"\033[1mTotal letter counts: \033[0m \n {letter_counts} \n")
print (f"\033[1mLetter positions: \033[0m \n {letter_positions} \n")

for letter in sorted(letter_counts, key=letter_counts.get, reverse=True):
    print(letter, letter_counts[letter])




