import random

def main():
    play_again = "yes"
    while play_again == "yes":
        guesses = 9
        solved_bool = False
        letters_guessed = []
        answer = get_answer()
        answer_list = [letters for letters in answer]
        hidden_answer = ["__" for letters in answer]
        while not solved_bool and guesses > 0:
            guess_letter_bool = False
            guess_letter = get_guess()
            letters_guessed += guess_letter 
            for i in range(len(answer)):
                if guess_letter == answer_list[i]:
                    hidden_answer[i] = guess_letter
                    guess_letter_bool = True
            if guess_letter_bool == True:
                print("Good guess!")
            else:
                guesses -= 1
                print("Bad Guess!")
            print(f"You have {guesses} left.")
            print(f"Hidden answer: {hidden_answer}")
            print(f"Letters guessed: {letters_guessed}")
            print ()
            if hidden_answer == answer_list:
                print("You solved the puzzle!")
                solved_bool = True
                play_again = input("Would you like to play again? Enter 'yes' or 'no'").lower()
            if hidden_answer != answer_list and guesses == 0:
                print("You Lose")
                print(f"The answer is {answer_list}")
                play_again = input("Would you like to play again? Enter 'yes' or 'no'").lower()
            
def get_answer():
    words = []
    file = open(r"C:\Users\enycz\Desktop\hangmanwords.txt","r")
    for line in file:
        for word in line.split():
            words.append(word.upper())
    file.close()
    answer = random.choice(words)
    return answer

def get_guess():
    while True:
        guess_letter = input("Guess a letter: ").upper()
        if ord(guess_letter) >= 65 and ord(guess_letter) <= 91:
            return guess_letter
        else:
            print("Try a different letter")

if __name__ == "__main__":
    main()




