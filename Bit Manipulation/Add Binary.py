"""
Time: O(max(m,n))  - m is len of string a and n is len of string b
Space: O(max(m,n)) - size of result obj
"""
def addBinary(a, b) -> str:
    result = ''
    carry = 0

    a, b = a[::-1], b[::-1]

    for i in range(max(len(a), len(b))):
        digitA = ord(a[i]) - ord('0') if i < len(a) else 0
        digitB = ord(b[i]) - ord('0') if i < len(b) else 0

        total = digitA + digitB + carry
        char = str(total % 2)
        result += char
        carry = total // 2

    if carry:
        result = '1' + result
    return result

print(addBinary('11','1'))      # -> '100'
print(addBinary('1010','1011')) # -> '10101'