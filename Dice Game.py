import random
import sys

def check_input(input_string):
    if input_string in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
           
def count_occurences(roll_results, value_to_count):
    count = 0
    for element in roll_results:
        if element == value_to_count:
            count += 1
    return count

def generate_dice_ascii(roll_results, DICE_ART):
    combined_lines = [""] * len(DICE_ART[1])  
    for result in roll_results:
        for i, line in enumerate(DICE_ART[result]):
            combined_lines[i] += line + "  "      
    for line in combined_lines:
        print(line)

def roll_dice(number_of_dice, dice_sides):
    roll_results = []
    for i in range(number_of_dice):
        roll_results.append(random.choice(dice_sides))
    return(roll_results)

def main():
    dice_sides = [1, 2, 3, 4, 5, 6]
    DICE_ART = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    number_of_dice = check_input(input("How many dice to roll?"))
    # number_of_dice = check_input(number_of_dice)
    roll_results = roll_dice(number_of_dice, dice_sides)
    generate_dice_ascii(roll_results, DICE_ART)
    for index in range(1, len(dice_sides)+1):
        count = count_occurences(roll_results, index)
        print(f"Value: {index}  Occurences: {count}")
    keep = input("Enter the position of dice to keep, separated by a comma: ")
    position_to_keep = keep.split(",")
    print(position_to_keep)
    second_roll_results = []
    for position in position_to_keep:
        position = int(position)
        second_roll_results.append(roll_results[position])
    print(second_roll_results)
        #second_roll_results.append(roll_dice(5 - len(second_roll_results), dice_sides))
    #print(second_roll_results)
    #generate_dice_ascii(second_roll_results, DICE_ART)
    

def check_input(input_string):
    if input_string in {"1", "2", "3", "4", "5", "6"}:
        return int(input_string)
    else:
        print("Please enter a number from 1 to 6.")
        raise SystemExit(1)
        
        
def count_occurences(roll_results, value_to_count):
    count = 0
    for element in roll_results:
        if element == value_to_count:
            count += 1
    return count


def generate_dice_ascii(roll_results, DICE_ART):
    combined_lines = [""] * len(DICE_ART[1])  
    for result in roll_results:
        for i, line in enumerate(DICE_ART[result]):
            combined_lines[i] += line + "  "      
    for line in combined_lines:
        print(line)


def roll_dice(number_of_dice, dice_sides):
    roll_results = []
    for i in range(number_of_dice):
        roll_results.append(random.choice(dice_sides))
    return(roll_results)


if __name__ == "__main__":
    main()


# In[ ]:




