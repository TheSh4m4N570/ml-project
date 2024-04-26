from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements from a requirements file.
    :param file_path:
    :return: requirements
    """
    requirements = []
    with open(file_path, 'r') as file:
        requirements = file.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
    author="Safwan JAWAD",
    author_email="safwan.cerberus@gmail.com",
    description="A short description of your package",
    url="https://github.com/TheSh4m4N570/ml-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)