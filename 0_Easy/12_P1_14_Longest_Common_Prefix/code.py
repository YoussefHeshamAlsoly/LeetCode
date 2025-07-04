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




# This was my original code

#     if len(strs) == 0:
#         return ""
#     elif len(strs) == 1:
#         return strs[0]
    
#     base = [i for i in reversed(strs[0])]
#     answer = []

#     for word in (strs[1:]):
#         print(f"Entering a word: {word}")
#         word = [i for i in reversed(word)]
#         for x in range(min(len(word), len(base))):
#             if base[-1]==word[-1]:
#                 answer.append(base[-1])
#                 base.pop()
#                 word.pop()
#                 print(f"base: {base}")
#                 print(f"word: {word}")
#             else:
#                 if answer:
#                     answer.pop()


#     return "".join(answer)



words = ["flower","flow","flight"]

print(f">{longestCommonPrefix(words)}<")