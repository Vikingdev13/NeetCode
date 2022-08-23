"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""
"""
Time: O(n)
Space: O(1)
"""
def plusOne(digits):
    # reverse the digits
    # note: this isnt necessary, but it's how I prefer to do it
    digits = digits[::-1]
    carry, i = 1, 0
    
    while carry:
        # while the index is less than the length of the array
        if i < len(digits):
            # if the current digit is a 9, we change it to a 0
            # carry val will stay at 1 since there is a 1 being carried to the next digit
            if digits[i] == 9:
                digits[i] = 0
            # else the digit is 0-8 and we can just increment it by 1
            # then we reset the carry to 0 since there wasnt a carry
            else:
                digits[i] += 1
                carry = 0
        # else the index is equal to or greater than the length of the array
        # and we append a 1 to the end(which will technically be the front once done)
        else:
            digits.append(1)
            carry = 0
        # dont forget to increment the index
        i += 1
    # return the original array but reverse it again since we reversed it at the beginning
    return digits[::-1]



if __name__ == "__main__":
    digits1 = [1,2,3]
    digits2 = [9,9,9]
    print(plusOne(digits1)) # -> [1,2,4]
    print(plusOne(digits2)) # -> [1,0,0,0]