# LeetCode Issue
# the following codes run fine on Python3 but not Python IDK why



def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    # salary = sorted(salary)
    
    # if len(salary) > 3:
    #     salary = salary[1:-1]
    #     return (sum(salary)/len(salary))
    # elif len(salary)==3:
    #     return salary[1]
    # else:
    #     return 0

    # x = len(salary) - 2
    # salary = sum(salary) - min(salary) - max(salary)
    # return salary/x

    # salary = sorted(salary)
    # salary.pop(0)
    # salary.pop()
    # return sum(salary)/len(salary)



salary = [48000,59000,99000,13000,78000,45000,31000,17000,39000,37000,93000,77000,33000,28000,4000,54000,67000,6000,1000,11000]
print(average(salary))