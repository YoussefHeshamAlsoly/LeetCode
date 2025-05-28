def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    # this is fast but IDEK how it works
    # res = 0
    # for c in s + t:
    #     res ^= ord(c)
    #     print(f'c: {c}, \t ord(c): {ord(c)}, \t res:{res}, \t chr(res):{chr(res)}')
    # return chr(res)
    
    s += t
    s = {c: s.count(c) for c in (s)}
    return next(key for key, value in s.items() if value == 1)


s = "ab"
t = "aeb"

print(findTheDifference(s, t))