def reverseWords(s:str):
    """
    :type s: str
    :rtype: str
    """
    s = s.split(" ")
    for i in range(len(s)):
        s[i] = "".join(reversed([x for x in s[i]]))
    
    return " ".join(s)

# s = "Let's take LeetCode contest"
# ans = "s'teL ekat edoCteeL tsetnoc"

s = "Mr Ding"
ans = "rM gniD"

print(reverseWords(s) == ans)
# print(reverseWords(s))