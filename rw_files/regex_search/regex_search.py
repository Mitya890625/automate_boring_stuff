"""
program which uses regex to check every file in folder and matchs with user's input and 
shows them in terminal
1. retrieve all files using Path object
2. iteritevly run through files and match pettern using regex
3. list all matches
"""
from pathlib import Path
import re

def retrieve_all_files_paths():
    p = Path.cwd()
    files_list = list(p.glob("*.txt"))
    return files_list
def match_pattern_in_all_files(files_list):
    for file_path in files_list:
        text_in_file = open(file_path)
        text = text_in_file.readline()
        regex_p = re.compile(r"{pattern}")
        mo = regex_p
