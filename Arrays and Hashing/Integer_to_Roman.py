"""
Given an integer, convert it to a roman numeral.
"""
"""
Time: O(1)
Space: O(1)
"""
def intToRoman(num):
    # initialize a list of tuples with pairs of values and their symbol
    digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), 
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), 
                  (5, "V"), (4, "IV"), (1, "I")]

    romanDigits = []
    # iterate through the tuple pairs
    for val, symb in digits:
        if num == 0:
            break
        # get the remainder of current num and val
        count, num = divmod(num, val)
        # append the count * symbol
        romanDigits.append(symb*count)
    # join the symbols together within the romanDigits list
    return "".join(romanDigits)

print(intToRoman(137))