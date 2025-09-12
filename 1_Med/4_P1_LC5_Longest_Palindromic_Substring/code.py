# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/

def longestPalindrome(s: str) -> str:
    # res = [""]*len(s)
    # left = 0
    # right = len(s)-1
    # counter = 0

    # while left <= right:
    #     if left == right and len([_ for _ in res if _!=""]):
    #         res[left] = s[left]
    #         break
    #     counter += 1
    #     if s[left] == s[right]:
    #         res[left] = s[left]
    #         res[right] = s[right]
    #         left += 1
    #         right -=1
    #     else:
    #         if counter%2:
    #             right = len(s)-1-counter
    #         else:
    #             left = len(s)-1-counter
    #         res = [""]*len(s)

    # return "".join(res).strip()
    # # return res

    if len(s) <= 1:
        return s
    
    Max_Len=1
    Max_Str=s[0]
    for i in range(len(s)-1):
        for j in range(i+1,len(s)):
            if j-i+1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                Max_Len = j-i+1
                Max_Str = s[i:j+1]

    return Max_Str


s = ["babad", "cbbd"]
for i in s:
    print(f"original:   {i}")
    print(f"Palindrome: {longestPalindrome(i)}")
    print()