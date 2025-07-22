def scoreOfString(s):
    """
    :type s: str
    :rtype: int
    """
    # s = [ord(i) for i in s]
    # total = 0
    # for i in range(len(s)):
    #     try:
    #         total += abs(s[i]-s[i+1])
    #     except IndexError:
    #         pass
    # return total

    return sum(abs(ord(s[i]) - ord(s[i+1])) for i in range(len(s) - 1))



s = "hello"
print(scoreOfString(s))