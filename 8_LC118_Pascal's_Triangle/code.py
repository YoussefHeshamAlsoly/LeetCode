# Runtime: 1ms Beats 26.56%
# Memory: 12.47MB Beats 55.60%



def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    # Base cases
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1] , [1,1]]
    
    else:
        made = [[1] , [1,1]]
        for row in range(2, numRows):
            current = [1]
        
            for element in range (len(made[row-1])):
                try:
                    current.append(made[row-1][element] + made[row-1][element+1])
                except IndexError:
                    current.append(1)
            
            made.append(current)
        return made


print(generate(5))