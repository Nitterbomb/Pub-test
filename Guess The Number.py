import random
attempts = 0
guess = int(0)
print("Enter the difficulty:")
print("1: 1 - 10")
print("2: 1 - 100")
print("3: 1 - 1000")
print("4: 1 - 10000")
select = int(input("Enter your selection 1 - 4:"))
randnum = random.randint(1,10**select)
while guess != randnum:
    guess = int(input("Enter your guess"))
    attempts = attempts+1
    if guess > randnum:
        print("Too High!")
    if guess < randnum:
        print("Too Low!")
    if guess == randnum:
        print("You Win!")
print("The number was {0} and it took you {1} guesses.".format(randnum,attempts))