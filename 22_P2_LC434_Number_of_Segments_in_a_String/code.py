
def countSegments(s):
    """
    :type s: str
    :rtype: int
    """
    # Best one yet
    s = sorted(s.split(" "), reverse=True)
    s = {c: s.count(c) for c in s}
    s.pop('', None)
    return sum(s.values())
    
    
    
    # counter = 0
    # s = sorted(s.split(" "), reverse=True)
    # for i in s:
    #     if i != "":
    #         counter += 1
    # return counter

    # s = sorted(s.split(" "), reverse=True)
    # try:
    #     while s[-1] == "":
    #         s.pop()
    # except:
    #     pass
    # return len(s)

print(countSegments('Hi this is soly      '))