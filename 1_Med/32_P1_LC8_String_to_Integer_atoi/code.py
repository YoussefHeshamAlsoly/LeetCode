# 8. String to Integer atoi
# https://leetcode.com/problems/string-to-integer-atoi/description/

RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"

def myAtoi(s: str) -> int:
    # 1. Constants for 32-bit integer limits
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # 2. Clean leading/trailing whitespace
    s = s.strip()
    if not s:
        return 0
    
    res, i, sign = 0, 0, 1
    
    # 3. Handle the sign
    if s[i] == '-':
        sign = -1
        i += 1
    elif s[i] == '+':
        i += 1
        
    # 4. Convert digits
    while i < len(s) and s[i].isdigit():
        digit = int(s[i])
        
        # Check for overflow before updating res
        # This is a standard way to handle 32-bit constraints
        if res > (INT_MAX - digit) // 10:
            return INT_MAX if sign == 1 else INT_MIN
        
        res = res * 10 + digit
        i += 1
        
    return res * sign


s = {"42" : 42,
    " -042" : -42,
    "1337c0d3" : 1337,
    "0-1" : 0,
    "words and 987" : 0,
    "     +004500" : 4500,
    "-5-": -5}


for test, correct_answer in s.items():
    my_answer = myAtoi(test)
    if my_answer == correct_answer:
        print(f"{GREEN}Passed{END} -> My answer is {my_answer}")
    else:
        print(f"{RED}Failed{END} -> {my_answer} : {correct_answer}")
