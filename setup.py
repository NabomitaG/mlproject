from setuptools import find_packages,setup
from typing import List

Hyp_E_DOT ='-e .'

def get_requirements(filePath:str)->List[str]:
    '''
    this will retrun list of requirements
    '''
    requirements =[]
    with open(filePath) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if Hyp_E_DOT in requirements:
            requirements.remove(Hyp_E_DOT)

    return requirements        


setup(
    name='mlproject',
    version='0.0.1',
    author='Nabomita',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)