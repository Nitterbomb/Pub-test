# hamming_distance.py finds the hamming distance between 2 strings

exit_command = ''
while exit_command != 'exit':                                           # program will continue to run until user enters 'exit'
    string_to_compare1 = ''
    string_to_compare2 = ''
    while string_to_compare1 == '' or string_to_compare2 == '':         # loops until user enters non-empty strings
        string_to_compare1 = input("Enter 1st string to compare: ")
        string_to_compare2 = input("Enter 2nd string to compare: ")

    if len(string_to_compare1) == len(string_to_compare2):              # string lengths must be equal
        hamming_distance = 0
        for i in range(len(string_to_compare1)):                        # loop through using i as the index of the strings
            if string_to_compare1[i] != string_to_compare2[i]:          # check equality of the characters at each index
                hamming_distance += 1
        print(f"The Hamming Distance between '{string_to_compare1}' and '{string_to_compare2}' is {hamming_distance}")
    else:
        print("Strings to compare are different lengths.")
        print("The Hamming Distance can not be calculated.")
    exit_command = input("Enter 'exit' to exit program or any other key to run again. ")






