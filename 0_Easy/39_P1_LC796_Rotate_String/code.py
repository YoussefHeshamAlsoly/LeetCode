def rotateString(s, goal):
    """
    :type s: str
    :type goal: str
    :rtype: bool
    """
    for _ in range(1, len(s)+1):
        print(type(s), goal)
        if s == goal:
            return True
        else:
            s = s[1:] + s[:1]
    return False

    # AMAZING
    # return len(s) == len(goal) and s in goal+goal 

s = "gcmbf"
g = "fgcmb"

print(rotateString(s, g))