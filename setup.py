"""
The setup file is used for setuptools, 
to define the configuration of the project, 
such as metadata, dependencies and more.
"""

from setuptools import find_packages,setup
from typing import List

def get_requirements()->List[str]:
    """
    This function will return the of requirements
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            # Read lines from tthe file
            lines = file.readlines()
            # Process the file
            for line in lines:
                requirements=line.strip()
                # Ignore the empty lines and -e .
                if requirements != "-e .":
                    requirement_lst.append(requirements)
    except FileNotFoundError:
        print('requirements.txt File not Found')
    
    return requirement_lst

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Oluoma Oji',
    author_email='oluomaoji@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)

