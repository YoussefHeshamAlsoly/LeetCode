# My code
# Runtime: 22ms Beats 12.35%
# Memory: 14.67MB Beats 6.81%


nums = [2,2,1,1,1,2,2]

dictionary_nums = {}
for i in range(len(nums)):
    dictionary_nums[nums[i]] = dictionary_nums.get(nums[i], 0) + 1

if max(dictionary_nums.values()) > len(nums)/2:
    print(max(dictionary_nums, key=dictionary_nums.get))
else:
    print ("0")

# For some reason, LeetCode does not care for checking if the result actually has the majority (n/2).
# So removing the final IF ELSE and just returning the second to last print line works with the following complexities.
# Runtime: 19ms Beats 17.35%
# Memory: 14.68MB Beats 6.81%