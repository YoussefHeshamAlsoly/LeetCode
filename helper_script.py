import os
from datetime import datetime
import re

# ===== CONFIG =====
directory = "./1_Med"
# ==================

def get_file_names_in_directory(directory_path):
    # Returns only directory names as per your original logic
    return [entry for entry in os.listdir(directory_path) 
            if os.path.isdir(os.path.join(directory_path, entry))]

def remove_chars(string_input: str):
    return string_input.replace("(", "").replace(")", "").replace(",", "")

files = get_file_names_in_directory(directory)

if not files:
    # Default for empty directory
    day_num = 1
    p_num = 1
else:
    # Sort files by their full path to find the one with the highest day number prefix
    full_paths = [os.path.join(directory, f) for f in files]
    last_folder_path = max(full_paths, key=os.path.getctime)
    last_folder_name = os.path.basename(last_folder_path)

    # Extract info from folder: "DayNum_PX_LC..."
    # Pattern looks for digits at start, then '_P' followed by digits
    match = re.match(r"(\d+)_P(\d+)_LC", last_folder_name)
    
    if match:
        last_day = int(match.group(1))
        last_p = int(match.group(2))
        
        # Check creation date
        creation_time = os.path.getctime(last_folder_path)
        last_date = datetime.fromtimestamp(creation_time).date()
        today_date = datetime.now().date()

        if last_date == today_date:
            day_num = last_day
            p_num = last_p + 1
        else:
            day_num = last_day + 1
            p_num = 1
    else:
        # Fallback if naming convention wasn't met
        day_num = len(files) + 1
        p_num = 1

# --- Folder Creation Logic ---
problem_name = input("Insert problem name: ")

# Construct the P string dynamically
p_string = f"_P{p_num}_LC"
local_dir_name = f"{day_num}{p_string}{problem_name.replace('.', '').replace(' ', '_')}"
local_dir_name = remove_chars(local_dir_name)

# Link generation
problem_parts = problem_name.split(".")
problem_link_name = problem_parts[1].lstrip().replace(" ", "-").lower() if len(problem_parts) > 1 else problem_name.lower().replace(" ", "-")
problem_link_name = remove_chars(problem_link_name)

full_link = f"https://leetcode.com/problems/{problem_link_name}/description/"

# Create directory and file
target_path = os.path.join(directory, local_dir_name)
os.mkdir(target_path)

colors = '''
RED = "\033[31m"
GREEN = "\033[32m"
END = "\033[0m"
'''

with open(f"{target_path}/code.py", "w") as file:
    file.write(f"# {problem_name}\n")
    file.write(f"# {full_link}\n\n\n\n")
    file.write(colors)
