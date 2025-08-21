def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    # A sorted string list will position the first and last word so that only those 2 are needed to be examined to determine
    # what is the longest prefix, as the last word will have the largest amount of letters for the prefix to actually exist
    strs = sorted(strs)
    answer = ""
    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if first[i] == last[i]:
            answer += first[i]
        else:
            return answer
    
    return answer


words = ["flower","flow","flight"]

print(f"{longestCommonPrefix(words)}")