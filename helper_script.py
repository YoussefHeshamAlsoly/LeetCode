import os
# ===== CONFIG =====
directory = "./1_Med"
# ==================


def get_file_names_in_directory(directory_path):
    file_names = []
    for entry in os.listdir(directory_path):
        full_path = os.path.join(directory_path, entry)
        if os.path.isdir(full_path):
            file_names.append(entry)
    return file_names

def remove_chars(string_input:str):
    try:
        string_input = string_input.replace("(", "").replace(")", "")
        string_input = string_input.replace(",", "")
    except Exception as e:
        pass
    return string_input



files = get_file_names_in_directory(directory)
last_file_num = max([int(i.split("_")[0]) for i in files])

day_num = str(last_file_num+1)


problem_name = input("Insert problem name: ")

local_dir_name = day_num+"_P1_LC"+problem_name[:].replace(".", "").replace(" ", "_")
local_dir_name = remove_chars(local_dir_name)

problem_link_name = problem_name.split(".")
problem_link_name = problem_link_name[1].lstrip().replace(" ", "-").lower()
problem_link_name = remove_chars(problem_link_name)


full_link = f"https://leetcode.com/problems/{problem_link_name}/description/"


os.mkdir(local_dir_name)
with open(f"{local_dir_name}/code.py", "w") as file:
    file.write(f"# {problem_name}\n")
    file.write(f"# {full_link}")
