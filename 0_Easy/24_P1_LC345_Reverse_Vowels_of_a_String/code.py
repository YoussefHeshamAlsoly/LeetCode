def reverseVowels(s:str):
    """
    :type s: str
    :rtype: str
    """
    s = list(s)
    vowel_list = []
    for i in range(len(s)):
        if s[i] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
            vowel_list.append(s[i])
            s[i] = '_'
    
    for i in range(len(s)):
        if s[i] == '_':
            s[i] = vowel_list.pop()

    return "".join(s)

s = 'IceCreAm'
print(reverseVowels(s))
