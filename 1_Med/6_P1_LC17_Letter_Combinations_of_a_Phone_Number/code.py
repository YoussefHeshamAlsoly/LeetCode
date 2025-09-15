# 17. Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
import itertools

def letterCombinations(digits: str) -> list[str]:
    if not digits:
        return []
    
    old_dial = {2:['a','b','c'],
                3:['d','e','f'],
                4:['g','h','i'],
                5:['j','k','l'],
                6:['m','n','o'],
                7:['p','q','r','s'],
                8:['t','u','v'],
                9:['w','x','y','z']}
    
    digits = [list(old_dial[int(_)]) for _ in digits]

    # could change the "combinations" to be "digits" to save some dumbass memory
    combinations = list(itertools.product(*digits))
    combinations = ["".join(_) for _ in combinations]

    return combinations

digits = "23"
print(letterCombinations(digits))