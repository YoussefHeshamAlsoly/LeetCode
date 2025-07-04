# Input: a = "11", b = "1"
# Output: "100"

a = "11"
b = "1"


def list_and_pad(string:str) -> list:
    final_list =  [int(x) for x in string]
    final_list = final_list[::-1]
    if len(final_list)>=4:
        pad = [0]*(4-len(final_list)%4)
        final_list.extend(pad)
    else:
        pad = [0]*(4-len(final_list))
        final_list.extend(pad)
    return final_list


def add_binary(list1:list, list2:list) -> str:
    answer = []
    carry = 0
    for i in range(len(list1)):
        if carry:
            if list1[i] and list2[i]:
                carry = 1
                answer.append(1)
            elif list1[i] or list2[i]:
                carry = 1
                answer.append(0)
            else:
                carry = 0
                answer.append(1)
            
        else:
            if list1[i] and list2[i]:
                carry = 1
                answer.append(0)
            elif list1[i] or list2[i]:
                carry = 0
                answer.append(1)
            else:
                carry = 0
                answer.append(0)

    # remove the padding
    while answer[-1]==0:
        if len(answer)==1:
            break
        answer.pop()

    final_str = ''.join(str(x) for x in answer[::-1])
    return final_str

aa = list_and_pad(a)
bb = list_and_pad(b)

answer = add_binary(aa, bb)
