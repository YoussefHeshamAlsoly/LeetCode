from collections import Counter

def firstUniqChar(s:str):
    """
    :type s: str
    :rtype: int
    """
    res = None
    s1 = Counter(s) # came in clutch!
    
    letter_count = [word for word, count in s1.items() if count == 1]
    for unique in letter_count:
        if res == None:
            res = s.index(unique)
        res = min(res, s.index(unique))

    return -1 if res==None else res

x = ["leetcode", "loveleetcode", "aabb"]

for i in x:
    print(f"i:{i},\nf(i):{firstUniqChar(i)}\n")