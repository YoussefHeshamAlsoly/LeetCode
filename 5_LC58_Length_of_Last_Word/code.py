string_input = "asldbnkl adbjn askljdbn adjb ankld jnas"

# x = [i for i in string_input.strip().split(" ")]

# print(len(x[-1]))

x = len ([i for i in string_input.strip().split(" ")][-1])
print(x)