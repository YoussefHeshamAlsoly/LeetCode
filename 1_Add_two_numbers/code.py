# given 2 lists

# list1 = [9,9,9,9,9,9,9]
# list2 = [9,9,9,9]

list1 = [2,4,3]
list2 = [5,6,4]


# Find which list is longer

longest = max(len(list1), len(list2))

shortest = min(len(list1), len(list2))

for i in range(longest):
    if i < shortest:
        list1[i] += list2[i]

# print (list1)

for x in range (len(list1)):
    if list1[x] > 9:
        try:
            list1[x+1] += list1[x]//10
        except IndexError:
            list1.insert(x+1, 1)
        list1[x] = list1[x]%10

# print(list1)


# This code works. But LeetCode has there own data type "ListNode" which is a dumb thing.
# So I used chatgpt to convert my code to adhere to the headache of listnodes
# here is the final code

# there is no actual need to create a class as leetcode already does that

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(node):
    length = 0
    while node:
        length += 1
        node = node.next
    return length

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    # Convert both linked lists to Python lists for easier manipulation
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



# This code beats 98% of other codes as it does not have any nested loops, so it has O(n)
# running for 2ms 
# BUTTTTT this solution takes more memory than 84.63% of the solutions.