# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/description/

RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"




# Worst code everrrrr
# class Solution:
#     def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
#         if len(candidates) == 1:
#             if candidates[0] == 0:
#                 return []
#             elif target % candidates[0] == 0:
#                 return [candidates * int(target/candidates[0])]
#             else:
#                 return []

#         res = []
#         temp_res = []
#         res.sort()

#         # check if the same number can recreate the target
#         for iter in candidates:
#             if target % iter == 0:
#                 res.append([iter] * int(target/iter))
        
        
#         for _ in range(len(candidates)):
#             if candidates[_] != 0:
#                 tie_breaker = abs(target-candidates[_])
#             else:
#                 tie_breaker = 1
#             total = candidates[_]
#             temp_res = [candidates[_]]
#             i = 0
#             looper = 0
#             popper = 0

#             while total < target:
#                 if looper > tie_breaker*2:
#                     break
#                 if i >= len(candidates):
#                     i = 0
#                     looper += 1
#                 if total + candidates[i] <= target:
#                     total += candidates[i]
#                     temp_res.append(candidates[i])
#                 else:
#                     popper = temp_res.pop()
#                     total -= popper
#                     i -= 1

#                 i += 1
#                 if total == target:
#                     temp_res.sort()
                    
#                     if temp_res in res:
#                         temp_res = []
#                         break
#                     elif sum(temp_res) == target:
#                         res.append(temp_res)
#                         temp_res = []
#                         break

#         return sorted(res)

# A -copied- working solution
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(start, target, path):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            for i in range(start, len(candidates)):
                backtrack(i, target - candidates[i], path + [candidates[i]])

        result = []
        candidates.sort()
        backtrack(0, target, [])
        return result


x = Solution()

candidates_list = [
        [2,3,6,7],
        [2,3,5],
        [2]
    ]

list_of_targets = [
        7,
        8,
        1
    ]

list_of_answers = [
        [[2,2,3],[7]],
        [[2,2,2,2],[2,3,3],[3,5]],
        [],
    ]

for iter in range (len(candidates_list)):
    print('\n')
    ans = x.combinationSum(candidates_list[iter], list_of_targets[iter])
    print("Sorted nums:   ", sorted(candidates_list[iter]))
    print("Target:        ", list_of_targets[iter])
    print("My answer:     ", ans)
    print("Actual answer: ", sorted(list_of_answers[iter]))
    if ans == list_of_answers[iter]:
        print(f"Verdict:        {GREEN}Pass{END}")
    else:
        print(f"Verdict:        {RED}Fail{END}")