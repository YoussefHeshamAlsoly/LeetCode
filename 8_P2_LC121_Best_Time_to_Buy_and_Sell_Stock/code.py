# Runtime: 91ms Beats 48.69%
# Memory: 18.98MB Beats 90.14%

def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not len(prices):
        return 0
    min_val = prices[0]
    min_ind = 0
    
    max_val = prices[0]
    max_ind = 0
    
    profit = 0

    for cur_ind, cur_val in enumerate(prices):
        print(f"=> cur_val: {cur_val} | cur_ind: {cur_ind}")
        print(f"=> min_val: {min_val} | min_ind: {min_ind}")
        print(f"=> max_val: {max_val} | max_ind: {max_ind}\n")

        if min_val > cur_val:
            min_val, min_ind = cur_val, cur_ind
            print("\tif min_val > cur_val:")
            print(f"\t========= min_val: {min_val} | min_ind: {min_ind} ========= \n")


        if max_ind < min_ind:
            max_ind, max_val = 0, 0
        if max_val < cur_val:
            max_val, max_ind = cur_val, cur_ind
            print("\tmax_val < cur_val")
            print(f"\t========= max_val: {max_val} | max_ind: {max_ind} ========= \n")
        
        if min_ind < max_ind:
            profit = max(profit, (max_val - min_val))
            print(f"\t$$$$ profit: {profit} $$$$")

    return profit


prices = [7,1,5,3,6,4]
print(maxProfit(prices))