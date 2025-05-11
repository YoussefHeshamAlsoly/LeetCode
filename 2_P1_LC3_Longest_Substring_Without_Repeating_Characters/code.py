# unfortunatlly my code failes in some tests


# input_string = "ijknabcdefgabhlmzxy"

input_string = "abcdahijklmna123456789"
input_string_to_list = list(input_string)
actual_dict = {}
str2set = set(input_string)


for i in str2set:
    actual_dict[i] = 0

current_total = 0

for j in range(len(input_string_to_list)):
    if current_total > len(input_string_to_list) - j:
        break

    for i in range(j, len(input_string_to_list)):
        print(actual_dict)
        if actual_dict[input_string_to_list[i]] == 0:
            actual_dict[input_string_to_list[i]] += 1

        else:
            current_total = max(current_total, sum(actual_dict.values()))
            print(f"here> i={i}, j={j}, current_total={current_total}")
            # print(f"input_string_to_list[i] = {input_string_to_list[i]}")
            # print(actual_dict)
            actual_dict.update(dict.fromkeys(actual_dict, 0))
            j = input_string_to_list.index(input_string_to_list[i])+1


print(current_total)