#!/usr/bin/python
from os import walk
from tabulate import tabulate
import re
import sys
import os


# FUNCTIONS
def validate(name):
  pattern = re.compile('[a-f][0-9]')
  special_characters = '"!@ #$%^&*()-+?=,<>/"ñÑáéíóú'
  if any(character in special_characters for character in name):
    print("ERROR")
    sys.exit(1)
  else:
    print("OK")

def run():
  for (dirpath, folders, filenames) in walk(base_path):
      problem_files.append(dirpath)
      # VALIDATE IF THE PATH IS EXCLUDED
      band = 0
      for exclude in excluded:
        if exclude in dirpath:
          band = 1
          break
      if band == 0:
        # VALIDATE NAMES ON FOLDERS
        for folder in folders:
          if folder not in excluded_folders:
            print(f"{folder} \t\t\t >>> ", end='')
            validate(folder)
        # VALIDATE NAMES ON FILES
        for  filename in filenames:
          if filename not in excluded_files:
            print(f"{filename} \t\t\t >>> ", end='')
            validate(filename)

if __name__ == "__main__":
  try:
    base_path = sys.argv[1]
  except:
    print("One parameter is required to analyze the folder and files names.")
    sys.exit(1)
  problem_files = []
  excluded_files = [".gitignore", ".gitmodules", "__init__.py", "LICENSE", "README.md"]
  excluded_folders = [".git", ".idea"]
  excluded = excluded_folders + excluded_files
  warnings = 0
  # RUN THE MAIN METHOD
  run()
