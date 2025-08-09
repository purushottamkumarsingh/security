"""
it is the important part of the project structure.
it is for the packaging and distributing python projects it  is used by the 
setup.py to define the project confugration of your project or metadata ,dependencies and more
"""
from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements_lst: List[str] = []
    try:
        with open("requirement.txt", 'r') as file:
            lines = file.readlines()  # reading each line of the file
            # process each line
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("file not found")

    return requirements_lst


setup(
    name='MLOPS_kRISH',
    version ='0.0.1',
    author= 'purushottam kumar singh',
    author_email='ravindrasingh813108@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements()
    

)


