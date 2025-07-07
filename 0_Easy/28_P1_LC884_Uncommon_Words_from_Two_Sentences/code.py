from collections import Counter

def uncommonFromSentences(s1:str, s2:str):
    """
    :type s1: str
    :type s2: str
    :rtype: List[str]
    """
    s1 = s1 + " " + s2
    s1 = s1.split(" ")
    s1 = Counter(s1)
    # s1 = {c: s1.count(c) for c in s1}
    return([i for i, j in s1.items() if j==1])

s1 = "this apple is sweet"
s2 = "this apple is sour"

print(uncommonFromSentences(s1, s2))