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


files = get_file_names_in_directory(directory)
last_file = files[-1].split("_")
day_num = str(int(last_file[0])+1)


problem_name = input("Insert problem name: ")
local_dir_name = day_num+"_P1_LC"+problem_name[:].replace(".", "").replace(" ", "_")

try:
    local_dir_name = local_dir_name.replace("(", "").replace(")", "")
    local_dir_name = local_dir_name.replace(",", "")
except Exception as e:
    pass

problem_link_name = problem_name.split(".")
problem_link_name = problem_link_name[1].lstrip().replace(" ", "-").lower()
try:
    problem_link_name = problem_link_name.replace("(", "").replace(")", "")
    problem_link_name = problem_link_name.replace(",", "")
except Exception as e:
    pass
full_link = f"https://leetcode.com/problems/{problem_link_name}/description/"


os.mkdir(local_dir_name)
with open(f"{local_dir_name}/code.py", "w") as file:
    file.write(f"# {problem_name}\n")
    file.write(f"# {full_link}")
