# Intuition
<!-- Describe your first thoughts on how to solve this problem. -->

# Approach
<!-- Describe your approach to solving the problem. -->

# Complexity
- Time complexity: 2 ms, better than 98.85%
<!-- Add your time complexity here, e.g. $$O(n)$$ -->

- Space complexity: 12.62 mb better than 15.37%
<!-- Add your space complexity here, e.g. $$O(n)$$ -->

# Code
```python []
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_length(node):
        length = 0
        while node:
            length += 1
            node = node.next
        return length

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def to_list(node):
            result = []
            while node:
                result.append(node.val)
                node = node.next
            return result

        def to_linked_list(lst):
            dummy = ListNode(0)
            current = dummy
            for val in lst:
                current.next = ListNode(val)
                current = current.next
            return dummy.next

        a = to_list(l1)
        b = to_list(l2)

        # Pad the shorter list with zeros
        max_len = max(len(a), len(b))
        a += [0] * (max_len - len(a))
        b += [0] * (max_len - len(b))

        # Add corresponding elements
        for i in range(max_len):
            a[i] += b[i]

        # Handle carries
        for i in range(max_len):
            if a[i] > 9:
                carry = a[i] // 10
                a[i] %= 10
                if i + 1 < max_len:
                    a[i + 1] += carry
                else:
                    a.append(carry)

        return to_linked_list(a)
```