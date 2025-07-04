# My final answer
def canConstruct(ransomNote, magazine):
    """
    :type ransomNote: str
    :type magazine: str
    :rtype: bool
    """
    letter_counts = {char: magazine.count(char) for char in set(magazine)}

    for i in range(len(ransomNote)):
        if ransomNote[i] in letter_counts and letter_counts[ransomNote[i]]>0:
            letter_counts[ransomNote[i]] -= 1
        else:
            return False
    return True

# # A somewhat fast method
# from collections import Counter
# def canConstruct(ransomNote, magazine):
#     return not (Counter(ransomNote) - Counter(magazine))



# # original idea
# def canConstruct(ransomNote, magazine):
#     """
#     :type ransomNote: str
#     :type magazine: str
#     :rtype: bool
#     """
#     magazine = sorted(magazine)
#     for i in range(len(ransomNote)):
#         if ransomNote[i] in magazine:
#             magazine.remove(ransomNote[i])
#         else:
#             return False
#     return True


note = 'bg'
mag = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print(canConstruct(note, mag))



