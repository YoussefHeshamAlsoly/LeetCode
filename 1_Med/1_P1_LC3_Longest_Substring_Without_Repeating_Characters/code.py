def lengthOfLongestSubstring(s: str) -> int:
    res = []
    act_len = 0
    
    for _ in range(len(s)):
        if s[_] not in res:
            res.append(s[_])
            act_len = max (act_len, len(res))
        
        else:
            res = res[res.index(s[_])+1:]
            res.append(s[_])

    return act_len

s = "aabaab!bb"

print(f"\nreturn {lengthOfLongestSubstring(s)}")