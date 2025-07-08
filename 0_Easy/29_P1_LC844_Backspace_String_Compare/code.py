def backspaceCompare(s:str, t:str):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    # s = [i for i in s]
    # s = {ind:let for ind, let in enumerate(s)}
    res = ()
    ans = []
    for i in (s+t):
        if (i in s and i not in t) and s[s.index(i)+1] == '#':
            pass
        elif (i in t and i not in s) and t[t.index(i)+1] == '#':
            pass
        elif i == '#':
            pass
        else:
            ans.append(i)
    
    print (ans)
    if ans[0:int(len(ans)/2)] == ans[int(len(ans)/2):]:
        return True
    else:
        return False


s = "ab##"
t = "c#d#"

print(backspaceCompare(s, t))