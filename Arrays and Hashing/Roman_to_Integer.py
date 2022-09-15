"""
Given a roman numeral, convert it to an integer.
"""
"""
Time: O(n)
Space: O(1)
"""
def romanToInt(str):
    symbols = {"I" : 1,
               "V" : 5,
               "X" : 10,
               "L" : 50,
               "C" : 100,
               "D" : 500,
               "M" : 1000
               }

    result = 0
    currVal, lastVal = 0, 0

    for i in range(len(str)):
        currVal = symbols.get(str[i], 0)
        result += currVal
        if lastVal < currVal:
            result -= lastVal * 2
        lastVal = currVal
    return result

print(romanToInt("V"))       # -> 5
print(romanToInt("XV"))      # -> 15
print(romanToInt("MMXXII"))  # -> 2022