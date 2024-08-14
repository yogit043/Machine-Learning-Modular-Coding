## for releasing a project as a module or a library or a package for this setup file is very important
## to build and distribute python packages
## contains information about the packages such as its name , version and dependencies as well as instructions for building and installing the package
from setuptools import setup , find_packages
from typing import List

PROJECT_NAME = "Machine Learning Project"
VERSION = "0.0.1"
DESCRIPTION = "This is our Machine Learning Project in modular coding"
AUTHOR = "Gurram Yogit"
AUTHOR_EMAIL = "yogit.gurram@gmail.com"
REQUIREMENTS_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME, 'r') as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n","") for requirement_name in requirement_list]
        
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(name=PROJECT_NAME,  # name of the package
      version=VERSION,  # version of the package
      description=DESCRIPTION,  # description of the package
      author=AUTHOR,  # author of the package
      author_email=AUTHOR_EMAIL,  # email of the author
      license='MIT',  # license of the package
      packages=find_packages(),
      install_requires = get_requirements_list()
)