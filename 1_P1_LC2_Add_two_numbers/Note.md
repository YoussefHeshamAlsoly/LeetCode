# Intuition
- idk man i just broke it down to sub-problems.
- first add the lists element-wise then  figure out how to do the carry-over.
- after adding, i used the modulus to break down any number greater than 9 into two numbers, the base stays in its place, and the extra is added to the next element in the list.
- if i faced an IndexError, that means that i reached the final element and still have an extra carried value, so just add an element to the end of the list and set it to 1.

# Stats
- Runtime: 48 ms Beats 5.22%
- Memory: 12.48 MB Beats 84.63%

# Code
```python []
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):


    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def listnode_to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        def list_to_listnode(lst):
            dummy = ListNode(0)
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next
        list1 = listnode_to_list(l1)
        list2 = listnode_to_list(l2)

        # Your logic, applied to plain lists
        if len(list1) >= len(list2):
            longest = list1
            shortest = list2
        else:
            longest = list2
            shortest = list1

        for i in range(len(longest)):
            if i < len(shortest):
                longest[i] += shortest[i]

        for x in range(len(longest)):
            if longest[x] > 9:
                try:
                    longest[x + 1] += longest[x] // 10
                except IndexError:
                    longest.insert(x + 1, 1)
                longest[x] = longest[x] % 10

        # Optional: print the intermediate result
        print(longest)

        return list_to_listnode(longest)
```