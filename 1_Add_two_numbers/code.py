# given 2 lists

# list1 = [9,9,9,9,9,9,9]
# list2 = [9,9,9,9]

list1 = [2,4,3,2,1]
list2 = [5,6,4,2,9,9]


# Find which list is longer

if len(list1) >= len(list2):
    longest = list1
    shortest = list2
else:
    longest = list2
    shortest = list1

for i in range(len(longest)):
    if i < len(shortest):
        longest[i] += shortest[i]

print (longest)
# print (list2)

for x in range (len(longest)):
    if longest[x] > 9:
        try:
            longest[x+1] += longest[x]//10
        except IndexError:
            longest.insert(x+1, 1)
        longest[x] = longest[x]%10

# print(longest)
# print(shortest)

# This code works. But LeetCode has there own data type "ListNode" which is a dumb thing.
# So I used chatgpt to convert my code to adhere to the headache of listnodes
# here is the final code



# there is no actual need to create a class as leetcode already does that
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):


    def addTwoNumbers(self, l1, l2):
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
"""