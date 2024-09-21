# CS 5010 601W Assg4 Eric Nycz
# Recursively called function that converts binary numbers to decimal numbers
def bin2dec(binNo, weight=0, result_as_decimal=0):
    if binNo // 10 == 0:             # conditional for the base case
        last_digit = binNo % 10
        result_as_decimal += last_digit * (2**weight)
        return result_as_decimal
    else:
        last_digit = binNo % 10
        result_as_decimal += last_digit * (2**weight)
        weight += 1
        binNo = binNo // 10
        return bin2dec(binNo, weight, result_as_decimal)

# Recursively called function that converts decimal numbers to binary numbers
def dec2bin(decNo, binary_digits=None):
    if binary_digits is None:       # conditional to create an empty list the first time the function is called
        binary_digits = []
    quotient = decNo // 2
    remainder = decNo % 2
    binary_digits.insert(0, str(remainder))
    if quotient == 0:               # conditional for the base case
        result_as_binary = int("".join(binary_digits))
        return result_as_binary
    else:
        return(dec2bin(quotient, binary_digits))

def main():   
    acceptable_binary_digits = {"0", "1"}
    with open("data-2.txt", "r") as datafile:
        for line in datafile:
            b_or_d, number = line.strip().split(" ")   # separates the type designation from the number and stores as strings
            if b_or_d == "b":
                if set(number) == acceptable_binary_digits or set(number) == {"0"} or set(number) == {"1"}:  # checks to make sure number is binary
                    number = int(number)
                    decimal_number = bin2dec(number)
                    binary_number = dec2bin(decimal_number)
                    print(f"Number given: {number} of type: {b_or_d}, converts to decimal: {decimal_number} and binary: {binary_number}")
                else:
                    print("Binary number does not consist of only 0's or 1's")
            elif b_or_d == "d":
                if number.isdigit():   # checks to make sure number is decimal
                    number = int(number)
                    binary_number = dec2bin(number)
                    decimal_number = bin2dec(binary_number)
                    print(f"Number given: {number} of type: {b_or_d}, converts to binary: {binary_number} and decimal: {decimal_number}")
                else:
                    print("Decimal number does not consist of only digits")
            else:
                print("Number is neither binary or decimal")

if __name__ == "__main__":
    main()