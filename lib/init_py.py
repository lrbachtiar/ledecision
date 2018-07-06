from pathlib import Path
import sys
import os

project_dir = Path(__file__).parents[1]
print("Root project dir is: {}".format(project_dir))

# os.chdir(project_dir)
folders_to_add = ["lib", "config", "data", "munge", "src"]
sys.path.insert(0, os.path.join(project_dir))

for folder in folders_to_add:
    sys.path.insert(0, os.path.join(project_dir / folder))
