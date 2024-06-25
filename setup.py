from setuptools import find_packages,setup
from typing import List

def get_requirements(file_path:str)->list[str]:
    '''
    this function return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[requ.replace("\n","") for requ in requirements]
        if "-e ." in requirements:
            requirements.remove("-e .")

    return requirements


setup(
    name="ML-Project",
    version="0.0.1",
    author="Abhishek",
    author_email="uniyalabhishek869@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")

)