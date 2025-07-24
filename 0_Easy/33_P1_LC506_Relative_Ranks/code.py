def findRelativeRanks(score):
    """
    :type score: List[int]
    :rtype: List[str]
    """
    dict_score = {val:index for index, val in enumerate(score)}
    score = sorted(score, reverse=True)

    ret = [0] * len(score)
    for x in range(len(score)):
        if x == 0:
            ret[dict_score[score[x]]] = "Gold Medal"
        elif x == 1:
            ret[dict_score[score[x]]] = "Silver Medal"
        elif x == 2:
            ret[dict_score[score[x]]] = "Bronze Medal"
        else:
            ret[dict_score[score[x]]] = str(x+1)
    
    return ret



score = [5,4,3,2,1]
print(findRelativeRanks(score))


# This version is so smart
"""
    def findRelativeRanks(score):
        sorted_scores = sorted(score, reverse=True)
        ranks = {sorted_scores[i]: str(i + 1) for i in range(len(score))}           # << amazing
        ranks[sorted_scores[0]] = "Gold Medal"
        if len(score) > 1:
            ranks[sorted_scores[1]] = "Silver Medal"
        if len(score) > 2:
            ranks[sorted_scores[2]] = "Bronze Medal"
        return [ranks[s] for s in score]
"""