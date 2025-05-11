
# # The following is a script that actually works

# class Solution(object):
#     def deleteDuplicates(self, head):
#         if not head:
#             return head
#         current = head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next

#         return head



# # And this code is purely mine and it does work, only on non-negative integers.
# # Aparently the "set" only sorts the non-negatives.
nums = [-2, -3, -1,0,0,0,0,3,3]
x = list(set(nums))
del nums[:]
nums.extend(x)
print(nums)