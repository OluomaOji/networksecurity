import os
from pathlib import Path


project_name = 'NetworkSecurity'

list_of_files = [
    '.github/workflows/main.yaml',
    'notebooks/research.ipynb',
    'Network_Data/Dataset/',
    'Dockerfile',
    'setup.py',
    f'{project_name}/__init__.py',
    f'{project_name}/components/__init__.py',
    f'{project_name}/constant/__init__py',
    f'{project_name}/logging/__init__.py',
    f'{project_name}/exception/__init__.py',
    f'{project_name}/utils/__init__.py',
    f'{project_name}/pipeline/__init__.py',
    f'{project_name}/cloud/cloud_file',
]

## For creating the folders and files
for filepath in list_of_files:
    filepath= Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
        print(f"Creating directory {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            print(f'Creating empt file: {filepath}')

    else:
        print(f'{filename} already exists')