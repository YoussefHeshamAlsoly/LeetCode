def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """

    index_map2 = {val: idx for idx, val in enumerate(list2)}
    
    min_sum = float('inf')
    result = []

    for idx1, val in enumerate(list1):
        if val in index_map2:
            total = idx1 + index_map2[val]
            if total < min_sum:
                min_sum = total
                result = [val]
            elif total == min_sum:
                result.append(val)

    return result
    
    # list1 = {loc1: list1.index(loc1) for loc1 in list1}
    # list2 = {loc2: list2.index(loc2) for loc2 in list2}
    # final = dict()
    
    # for key, val in list1.items():
    #     if key in list2:
    #         final[key] = val + list2[key]
    
    # keys = [k for k, v in final.items() if v == min(final.values())]
    # return(keys)

list1 = ["happy","sad","good"]
list2 = ["sad","happy","good"]

print(findRestaurant(list1, list2))